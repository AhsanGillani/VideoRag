"""
Vercel entrypoint.

Just re-exports the existing ASGI app from config.asgi so
all Django wiring stays in the main project.
On Vercel, copy bundled db.sqlite3 to /tmp once so the DB is writable (sessions, admin).
"""
import os
import shutil

if os.environ.get('VERCEL'):
    _tmp_db = '/tmp/db.sqlite3'
    if not os.path.exists(_tmp_db):
        _project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        _bundled_db = os.path.join(_project_root, 'db.sqlite3')
        if os.path.exists(_bundled_db):
            shutil.copy2(_bundled_db, _tmp_db)

from config.asgi import application as app


