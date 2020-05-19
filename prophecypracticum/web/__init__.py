import os

from flask import Flask

from . import db
from . import auth
from . import practicum
from . import admin


def create_app(test_config=None):
    """Create and configure the app."""
    app = Flask(__name__, instance_relative_config=True)
    # override SECRET_KEY when deployed
    database_path = os.path.join(app.instance_path, "prophephypracticum.sqlite")
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{database_path}'
    app.config.from_mapping(SECRET_KEY='dev', DATABASE=os.path.join(app.instance_path, 'prophephypracticum.sqlite'))
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    if test_config is None:
        # Load the instance config, if it exists, when not testing. - eg the SECRET_KEY can be in config.py
        app.config.from_pyfile('config.py', silent=True)
    else:
        # Load the test config if passed in.
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello - used later for unit testing
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    app.register_blueprint(auth.bp)
    app.register_blueprint(practicum.bp)
    app.register_blueprint(admin.bp)
    app.add_url_rule('/', endpoint='index')

    db.db.init_app(app)

    @app.before_first_request
    def create_tables():
        db.db.create_all()

    return app
