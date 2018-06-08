import os
from flask import Flask


def create_app(test_config=None):
    '''
    create and configure your application
    '''
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        # load the instance config when not testing
        pass
    else:
        # load the test config
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # simple home page that says hello
    @app.route('/', methods=['GET'])
    def index():
        return 'Hello World!<br/>You are home'

    return app
