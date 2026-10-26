"""데이터 저장소 (SQLite). 기획서 4장의 8가지 대상을 테이블로 둔다."""
import sqlite3
from pathlib import Path

from flask import g

DB_PATH = Path(__file__).parent / "data" / "pmo.db"

SCHEMA = """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    org TEXT,
    is_admin INTEGER NOT NULL DEFAULT 0          -- 시스템 관리자(PMO)
);
CREATE TABLE IF NOT EXISTS projects (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    version TEXT,                                 -- 연결된 일감 범위 (엑셀 request version 기준)
    start_date TEXT,
    end_date TEXT,
    created_by INTEGER REFERENCES users(id),
    created_at TEXT NOT NULL DEFAULT (datetime('now','localtime'))
);
CREATE TABLE IF NOT EXISTS members (
    project_id INTEGER NOT NULL REFERENCES projects(id) ON DELETE CASCADE,
    user_id INTEGER NOT NULL REFERENCES users(id),
    role TEXT NOT NULL CHECK (role IN ('manager','member','viewer')),
    PRIMARY KEY (project_id, user_id)
);
CREATE TABLE IF NOT EXISTS issues (                -- 일감
    jira_key TEXT PRIMARY KEY,
    summary TEXT, status TEXT, reporter TEXT, assignee TEXT,
    component TEXT, poc TEXT, request_version TEXT,
    created_date TEXT, updated_date TEXT, jira_url TEXT,
    missing INTEGER NOT NULL DEFAULT 0           -- 최근 엑셀에서 빠짐
);
CREATE TABLE IF NOT EXISTS issue_history (
    id INTEGER PRIMARY KEY,
    jira_key TEXT NOT NULL, field TEXT NOT NULL,
    before TEXT, after TEXT, changed_at TEXT, upload_id INTEGER
);
CREATE TABLE IF NOT EXISTS milestones (
    id INTEGER PRIMARY KEY,
    version TEXT, name TEXT, start_date TEXT, end_date TEXT, status TEXT
);
CREATE TABLE IF NOT EXISTS alert_rules (
    id TEXT PRIMARY KEY,                          -- A1~A6
    name TEXT, target TEXT, timing TEXT, channels TEXT
);
CREATE TABLE IF NOT EXISTS notifications (
    id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(id),
    project_id INTEGER REFERENCES projects(id) ON DELETE SET NULL,
    rule_id TEXT, dedup_key TEXT, message TEXT, link TEXT, channels TEXT,
    sent_at TEXT NOT NULL DEFAULT (datetime('now','localtime')),
    read_at TEXT,
    UNIQUE (user_id, dedup_key)                   -- 같은 변경으로 두 번 보내지 않음
);
CREATE TABLE IF NOT EXISTS uploads (
    id INTEGER PRIMARY KEY,
    filename TEXT, uploaded_by INTEGER REFERENCES users(id),
    uploaded_at TEXT NOT NULL DEFAULT (datetime('now','localtime')),
    new_count INTEGER, changed_count INTEGER, missing_count INTEGER,
    confirmed INTEGER NOT NULL DEFAULT 0
);
CREATE TABLE IF NOT EXISTS audit_log (            -- 접근 기록
    id INTEGER PRIMARY KEY,
    user_id INTEGER, action TEXT, detail TEXT,
    at TEXT NOT NULL DEFAULT (datetime('now','localtime'))
);
"""

# 1단계 시제품용 가짜 사용자 (실제 인물 아님)
SAMPLE_USERS = [
    ("김피엠", "pmo.kim@example.com", "PMO팀", 1),
    ("이피엠", "pmo.lee@example.com", "PMO팀", 1),
    ("박기획", "br.park@example.com", "서비스기획팀", 0),
    ("최개발", "dev.choi@example.com", "Web플랫폼개발팀", 0),
    ("정모바일", "mobile.jung@example.com", "모바일개발팀", 0),
    ("한사업", "biz.han@example.com", "커머스사업팀", 0),
]


def get_db():
    if "db" not in g:
        DB_PATH.parent.mkdir(exist_ok=True)
        g.db = sqlite3.connect(DB_PATH)
        g.db.row_factory = sqlite3.Row
        g.db.execute("PRAGMA foreign_keys = ON")
    return g.db


def close_db(_exc=None):
    db = g.pop("db", None)
    if db is not None:
        db.close()


def init_db():
    db = get_db()
    db.executescript(SCHEMA)
    if db.execute("SELECT COUNT(*) FROM users").fetchone()[0] == 0:
        db.executemany(
            "INSERT INTO users (name, email, org, is_admin) VALUES (?,?,?,?)", SAMPLE_USERS
        )
    db.commit()


def audit(user_id, action, detail=""):
    get_db().execute(
        "INSERT INTO audit_log (user_id, action, detail) VALUES (?,?,?)", (user_id, action, detail)
    )
