"""Handle database connections for the application."""

import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(current_app.config['DATABASE'], detect_types=sqlite3.PARSE_DECLTYPES)
        g.db.row_factory = sqlite3.Row  # causes the row data to behave like a dictionary

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()


def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:  # open resource allows you not to worry about file path
        db.executescript(f.read().decode('utf8'))


@click.command('init-db')  # allows a command to be run from the cli
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')


def init_app(app):
    app.teardown_appcontext(close_db)  # it can clean up
    app.cli.add_command(init_db_command)  # now this command can be called from the flask command