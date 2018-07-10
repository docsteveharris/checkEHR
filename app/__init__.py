from flask import Flask
from config import config
from flask_bootstrap import Bootstrap
from flask_cloudant import FlaskCloudant
import requests
import sys

# let's try using the flask_cloudant extension
# pip install your version
# pip install git+https://github.com/docsteveharris/flask-cloudant.git@cloudant
# then delete flask_cloudant dir and symbolic link in your own

bootstrap = Bootstrap()
db = FlaskCloudant()


def create_app(config_name):
    '''
    create and configure your application
    '''
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # bootstrap
    bootstrap.init_app(app)

    # cloudant/couchdb
    try:
        couch_url = app.config['COUCH_URL']
        requests.get(couch_url)
        db.init_app(app)
    except requests.ConnectionError as e:
        print('*** *******************************************')
        print('*** Did you forget to start the couchDB server?')
        print('*** *******************************************')
        sys.exit(e)

    # attach routes and custom error pages here

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
