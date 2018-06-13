from flask import Flask
from config import config
from flask_bootstrap import Bootstrap


def create_app(config_name):
    '''
    create and configure your application
    '''
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    Bootstrap(app)
    # - [ ] @TODO: (2018-06-13) @resume flask_bootstrap recommendations
    # https://github.com/mbr/flask-bootstrap/blob/master/sample_app/__init__.py

    # attach routes and custom error pages here

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
