import pytest
from app import create_app, db
from flask import g, current_app as app
import cloudant


# see https://www.blazemeter.com/blog/improve-your-selenium-webdriver-tests-
# with-pytest
@pytest.fixture(scope='class')
def driver_init(request):
    from selenium import webdriver
    web_driver = webdriver.Firefox()
    request.cls.driver = web_driver
    yield
    web_driver.quit()


@pytest.fixture(scope='class')
def element_one():
    """Extracts first element from testing couchDB for use in testing"""
    # - [ ] @TODO: (2018-07-21) @later programmatically create your own db
    with cloudant.couchdb(
            'testyMcTestFace',
            'testyMcTestFace',
            url='http://127.0.0.1:5984') as couch:
        couch.connect()
        db = couch['chkehr-test']
        result = cloudant.result.Result(db.all_docs, include_docs=True)
        element_one = result[0][0]

        yield element_one

        couch.disconnect()


@pytest.fixture(scope='session')
def client():
    """An application for the tests."""
    _app = create_app('testing')
    ctx = _app.test_request_context()
    ctx.push()
    # Push the database into the request global context g
    g.db = db
    client = _app.test_client()

    yield client

    ctx.pop()


@pytest.fixture(scope='function')
def couch_url(client):
    couch_url = '{}{}:{}@{}'.format(
        app.config['_PROTOCOL'],
        app.config['COUCH_USER'],
        app.config['COUCH_PWD'],
        app.config['_COUCH_URL']
    )

    yield couch_url
