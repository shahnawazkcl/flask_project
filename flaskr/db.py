import sqlite3
import click

from flask import current_app, g

# store and resue the connection to the database
def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory=sqlite3.Row

    return g.db

# check the if the db open then close before request.
def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

