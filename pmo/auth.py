"""로그인. 1단계는 가짜 로그인(이름 선택), 2단계에서 이 파일만 SSO로 교체한다.

화면 코드는 current_user()와 login_required만 사용하므로 교체해도 영향이 없다.
"""
from functools import wraps

from flask import abort, g, redirect, session, url_for

from db import get_db


def current_user():
    if "user" not in g:
        uid = session.get("user_id")
        g.user = (
            get_db().execute("SELECT * FROM users WHERE id = ?", (uid,)).fetchone() if uid else None
        )
    return g.user


def login_as(user_id):
    session.clear()
    session["user_id"] = user_id


def logout():
    session.clear()


def login_required(view):
    @wraps(view)
    def wrapped(*args, **kwargs):
        if current_user() is None:
            return redirect(url_for("login"))
        return view(*args, **kwargs)
    return wrapped


def admin_required(view):
    @wraps(view)
    @login_required
    def wrapped(*args, **kwargs):
        if not current_user()["is_admin"]:
            abort(403)
        return view(*args, **kwargs)
    return wrapped
