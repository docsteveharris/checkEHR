from flask import Flask
from config import config


def create_app(config_name):
    '''
    create and configure your application
    '''
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # attach routes and custom error pages here

    return app
