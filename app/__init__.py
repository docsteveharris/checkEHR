from flask import Flask


def create_app(test_config=None):
    '''
    create and configure your application
    '''
    app = Flask(__name__)

    # simple home page that says hello
    @app.route('/')
    def index():
        return 'Hello World!<br/>You are home'

    return app
