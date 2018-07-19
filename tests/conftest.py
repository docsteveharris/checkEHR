import pytest
from app import create_app


# @pytest.fixture(scope='session')
# def app():
#     app = create_app('testing')
#     return app


@pytest.fixture(scope='session')
def app():
    """An application for the tests."""
    _app = create_app('testing')
    ctx = _app.test_request_context()
    ctx.push()

    yield _app

    ctx.pop()


@pytest.fixture(scope='function')
def couch_url(app):
    couch_url = '{}{}:{}@{}'.format(
        app.config['_PROTOCOL'],
        app.config['COUCH_USER'],
        app.config['COUCH_PWD'],
        app.config['_COUCH_URL']
    )

    yield couch_url
