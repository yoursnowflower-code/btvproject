"""PMO 일감 트래킹·알림 시스템 — 1단계 시제품.

실행: python app.py  →  http://localhost:5000
"""
import os

from flask import Flask, abort, flash, redirect, render_template, request, url_for

import auth
from auth import admin_required, current_user, login_required
from db import audit, close_db, get_db, init_db

app = Flask(__name__)
app.secret_key = os.environ.get("PMO_SECRET_KEY", "dev-only-change-me")
app.teardown_appcontext(close_db)

ROLE_LABELS = {"manager": "프로젝트 관리자", "member": "멤버", "viewer": "열람자"}
# 1차는 관리자·멤버만 지정 가능 (열람자는 2차, 11장 8번)
ASSIGNABLE_ROLES = ("manager", "member")


@app.context_processor
def inject_globals():
    user = current_user()
    unread = 0
    if user:
        unread = get_db().execute(
            "SELECT COUNT(*) FROM notifications WHERE user_id = ? AND read_at IS NULL", (user["id"],)
        ).fetchone()[0]
    return {"user": user, "unread_total": unread, "ROLE_LABELS": ROLE_LABELS}


def visible_projects(user):
    """시스템 관리자는 전체, 그 외는 등록된 프로젝트만 본다 (3장 원칙)."""
    db = get_db()
    base = """
        SELECT p.*, m.role,
          (SELECT name || '|' || end_date FROM milestones ms
             WHERE ms.version = p.version AND ms.end_date >= date('now','localtime')
             ORDER BY ms.end_date LIMIT 1) AS next_ms,
          (SELECT COUNT(*) FROM notifications n
             WHERE n.project_id = p.id AND n.user_id = :uid AND n.read_at IS NULL) AS unread,
          (SELECT COUNT(*) FROM members mm WHERE mm.project_id = p.id) AS member_count
        FROM projects p
        LEFT JOIN members m ON m.project_id = p.id AND m.user_id = :uid
    """
    where = "" if user["is_admin"] else "WHERE m.user_id IS NOT NULL"
    return db.execute(f"{base} {where} ORDER BY p.created_at DESC", {"uid": user["id"]}).fetchall()


def get_project_or_404(project_id):
    user = current_user()
    project = get_db().execute(
        """SELECT p.*, m.role FROM projects p
           LEFT JOIN members m ON m.project_id = p.id AND m.user_id = ?
           WHERE p.id = ?""",
        (user["id"], project_id),
    ).fetchone()
    # 등록되지 않은 사람에게는 프로젝트가 존재하는지도 알리지 않는다
    if project is None or (not user["is_admin"] and project["role"] is None):
        abort(404)
    return project


def can_manage(project):
    """시스템 관리자 또는 해당 프로젝트의 관리자."""
    return bool(current_user()["is_admin"]) or project["role"] == "manager"


def get_managed_project_or_403(project_id):
    project = get_project_or_404(project_id)
    if not can_manage(project):
        abort(403)
    return project


def read_project_form():
    form = {k: request.form.get(k, "").strip() for k in ("name", "version", "start_date", "end_date")}
    errors = []
    if not form["name"]:
        errors.append("프로젝트 이름을 입력해 주세요.")
    if form["start_date"] and form["end_date"] and form["start_date"] > form["end_date"]:
        errors.append("종료일이 시작일보다 빠릅니다.")
    return form, errors


# ---- S1 로그인 -------------------------------------------------------------

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user_id = request.form.get("user_id", type=int)
        if user_id and get_db().execute("SELECT 1 FROM users WHERE id = ?", (user_id,)).fetchone():
            auth.login_as(user_id)
            return redirect(url_for("project_list"))
        flash("사용자를 선택해 주세요.")
    users = get_db().execute("SELECT * FROM users ORDER BY is_admin DESC, name").fetchall()
    return render_template("login.html", users=users)


@app.route("/logout")
def logout():
    auth.logout()
    return redirect(url_for("login"))


# ---- S2 프로젝트 목록 / 만들기 / 수정 / 삭제 ------------------------------------

@app.route("/")
@login_required
def project_list():
    return render_template("projects.html", projects=visible_projects(current_user()))


@app.route("/projects/new", methods=["GET", "POST"])
@admin_required
def project_new():
    form, errors = {}, []
    if request.method == "POST":
        form, errors = read_project_form()
        if not errors:
            db = get_db()
            user = current_user()
            cur = db.execute(
                "INSERT INTO projects (name, version, start_date, end_date, created_by) VALUES (?,?,?,?,?)",
                (form["name"], form["version"] or None, form["start_date"] or None,
                 form["end_date"] or None, user["id"]),
            )
            # 만든 사람은 자동으로 프로젝트 관리자로 등록
            db.execute("INSERT INTO members VALUES (?,?, 'manager')", (cur.lastrowid, user["id"]))
            audit(user["id"], "project.create", form["name"])
            db.commit()
            flash(f"‘{form['name']}’ 프로젝트를 만들었습니다.")
            return redirect(url_for("project_list"))
    return render_template("project_form.html", form=form, errors=errors, project=None)


@app.route("/projects/<int:project_id>")
@login_required
def project_detail(project_id):
    # S3 현황 화면은 순서 3·7에서 채운다
    project = get_project_or_404(project_id)
    return render_template("project_detail.html", project=project, can_manage=can_manage(project))


@app.route("/projects/<int:project_id>/edit", methods=["GET", "POST"])
@admin_required
def project_edit(project_id):
    project = get_project_or_404(project_id)
    form, errors = dict(project), []
    if request.method == "POST":
        form, errors = read_project_form()
        if not errors:
            db = get_db()
            db.execute(
                "UPDATE projects SET name=?, version=?, start_date=?, end_date=? WHERE id=?",
                (form["name"], form["version"] or None, form["start_date"] or None,
                 form["end_date"] or None, project_id),
            )
            audit(current_user()["id"], "project.update", f"{project_id}:{form['name']}")
            db.commit()
            flash("프로젝트 정보를 저장했습니다.")
            return redirect(url_for("project_list"))
    return render_template("project_form.html", form=form, errors=errors, project=project)


@app.route("/projects/<int:project_id>/delete", methods=["POST"])
@admin_required
def project_delete(project_id):
    project = get_project_or_404(project_id)
    db = get_db()
    db.execute("DELETE FROM projects WHERE id = ?", (project_id,))
    audit(current_user()["id"], "project.delete", f"{project_id}:{project['name']}")
    db.commit()
    flash(f"‘{project['name']}’ 프로젝트를 삭제했습니다.")
    return redirect(url_for("project_list"))


# ---- S4 프로젝트 설정: 멤버 관리 (F3) ---------------------------------------------

@app.route("/projects/<int:project_id>/settings")
@login_required
def project_settings(project_id):
    project = get_managed_project_or_403(project_id)
    db = get_db()
    members = db.execute(
        """SELECT u.*, m.role FROM members m JOIN users u ON u.id = m.user_id
           WHERE m.project_id = ? ORDER BY m.role = 'manager' DESC, u.name""",
        (project_id,),
    ).fetchall()
    candidates = db.execute(
        """SELECT * FROM users WHERE id NOT IN (SELECT user_id FROM members WHERE project_id = ?)
           ORDER BY name""",
        (project_id,),
    ).fetchall()
    return render_template("project_settings.html", project=project, members=members,
                           candidates=candidates, roles=ASSIGNABLE_ROLES)


def manager_count(project_id):
    return get_db().execute(
        "SELECT COUNT(*) FROM members WHERE project_id = ? AND role = 'manager'", (project_id,)
    ).fetchone()[0]


def member_row(project_id, user_id):
    return get_db().execute(
        """SELECT u.name, m.role FROM members m JOIN users u ON u.id = m.user_id
           WHERE m.project_id = ? AND m.user_id = ?""",
        (project_id, user_id),
    ).fetchone()


@app.route("/projects/<int:project_id>/members", methods=["POST"])
@login_required
def member_add(project_id):
    get_managed_project_or_403(project_id)
    user_id = request.form.get("user_id", type=int)
    role = request.form.get("role")
    db = get_db()
    target = db.execute("SELECT * FROM users WHERE id = ?", (user_id,)).fetchone()
    if target is None or role not in ASSIGNABLE_ROLES:
        flash("추가할 사람과 역할을 선택해 주세요.")
    elif member_row(project_id, user_id):
        flash(f"{target['name']}님은 이미 멤버입니다.")
    else:
        # 추가한 시점부터 알림 대상이 된다 (알림은 순서 5·6에서 members 기준으로 발송)
        db.execute("INSERT INTO members VALUES (?,?,?)", (project_id, user_id, role))
        audit(current_user()["id"], "member.add", f"{project_id}:{user_id}:{role}")
        db.commit()
        flash(f"{target['name']}님을 {ROLE_LABELS[role]}(으)로 추가했습니다.")
    return redirect(url_for("project_settings", project_id=project_id))


@app.route("/projects/<int:project_id>/members/<int:user_id>/role", methods=["POST"])
@login_required
def member_role(project_id, user_id):
    get_managed_project_or_403(project_id)
    role = request.form.get("role")
    row = member_row(project_id, user_id)
    if row is None or role not in ASSIGNABLE_ROLES:
        abort(400)
    if row["role"] == "manager" and role != "manager" and manager_count(project_id) == 1:
        flash("프로젝트 관리자가 최소 1명은 있어야 합니다.")
    elif row["role"] != role:
        db = get_db()
        db.execute("UPDATE members SET role = ? WHERE project_id = ? AND user_id = ?",
                   (role, project_id, user_id))
        audit(current_user()["id"], "member.role", f"{project_id}:{user_id}:{row['role']}->{role}")
        db.commit()
        flash(f"{row['name']}님의 역할을 {ROLE_LABELS[role]}(으)로 바꿨습니다.")
    return redirect(url_for("project_settings", project_id=project_id))


@app.route("/projects/<int:project_id>/members/<int:user_id>/remove", methods=["POST"])
@login_required
def member_remove(project_id, user_id):
    get_managed_project_or_403(project_id)
    row = member_row(project_id, user_id)
    if row is None:
        abort(404)
    if row["role"] == "manager" and manager_count(project_id) == 1:
        flash("마지막 프로젝트 관리자는 제거할 수 없습니다. 다른 관리자를 먼저 지정해 주세요.")
        return redirect(url_for("project_settings", project_id=project_id))
    db = get_db()
    # 제거하면 즉시 프로젝트 열람과 알림이 중단된다
    db.execute("DELETE FROM members WHERE project_id = ? AND user_id = ?", (project_id, user_id))
    audit(current_user()["id"], "member.remove", f"{project_id}:{user_id}")
    db.commit()
    flash(f"{row['name']}님을 프로젝트에서 제거했습니다.")
    if user_id == current_user()["id"] and not current_user()["is_admin"]:
        return redirect(url_for("project_list"))
    return redirect(url_for("project_settings", project_id=project_id))


# ---- 상단 메뉴의 아직 만들지 않은 화면 ---------------------------------------------

@app.route("/inbox")
@login_required
def inbox():
    return render_template("placeholder.html", title="알림함", step="5")


@app.route("/settings")
@login_required
def my_settings():
    return render_template("placeholder.html", title="내 설정", step="8")


with app.app_context():
    init_db()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)
