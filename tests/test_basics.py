# - [ ] @TODO: (2018-06-13) @resume @refactor switch to flask pytest layout
# # http://flask.pocoo.org/docs/1.0/testing/
# import pytest
from flask import url_for, g, Flask
from app import db
import requests
from cloudant import couchdb


def test_smoke():
    pass


def test_pytest_flask_app(app):
    '''Check the pytest-flask extension has generated an app via the fixture
    declared in conftest.py'''
    assert isinstance(app, Flask)


def test_app_is_testing(app):
    assert app.config['TESTING'] is True


def test_index_returns_html_and_app_name(app):
    # - [ ] @TODO: (2018-07-19) @fixme work out better way of getting db into g
    g.db = db  # forces db into request context
    res = app.test_client().get(url_for('main.index'))
    assert res.status_code == 200
    res = res.get_data(as_text=True)
    assert '<html>' in res
    assert '</html>' in res
    # check title corresponds to app
    assert 'checkEHR' in res


def test_couchdb_is_running(app):
    couch_url = app.config['COUCH_URL']
    res = requests.get(couch_url)
    assert res.status_code == 200
    res_json = res.json()
    assert 'couchdb' in res_json.keys()
    assert res_json['version'], '2.1.1'


def test_login_to_couchdb_needs_credentials(app):
    # No credentials
    couch_url = app.config['COUCH_URL']
    res = requests.put(couch_url + '/testing_db_via_requests')
    assert res.status_code == 401


def test_login_to_couchdb_with_credentials(app, couch_url):
    res = requests.get(couch_url)
    assert res.status_code == 200

    # proof of principle that credentials allow PUT
    # try to delete the database
    try:
        res = requests.delete(couch_url + '/testing_db_via_requests')
        res.raise_for_status()
    except requests.exceptions.HTTPError:
        res = requests.put(couch_url + '/testing_db_via_requests')
        assert res.status_code == 201
    finally:
        requests.delete(couch_url + '/testing_db_via_requests')


def test_cloudant_api_works(app):
    '''Try connection with cloudant API rather than requests'''
    with couchdb(app.config['COUCH_USER'],
                 app.config['COUCH_PWD'],
                 url=app.config['COUCH_URL']
                 ) as client:
        assert client.all_dbs() is not None
        # self.assertIsNotNone(client.all_dbs())
        # db = client.create_database('testing_db_via_cloudant')
        # self.assertTrue('testing_db_via_cloudant' in client.all_dbs())
        # self.assertTrue(db.exists())
        # client.delete_database('testing_db_via_cloudant')

#     def test_cloudant_receives_configuration_from_flask(self):
#         '''Use the Flask configuration to connect to the correct database'''
#         from cloudant import couchdb
#         with couchdb(
#                 current_app.config['COUCH_USER'],
#                 current_app.config['COUCH_PWD'],
#                 url=current_app.config['COUCH_URL']) as client:
#             db = client.create_database('testing_db_via_flask')
#             self.assertTrue('testing_db_via_flask' in client.all_dbs())
#             self.assertTrue(db.exists())
#             client.delete_database('testing_db_via_flask')


# class TestFlaskCloudant(unittest.TestCase):
#     '''Test that FlaskCloudant extension is present and works'''

#     def setUp(self):
#         '''Creates a version of the Flask application for testing'''
#         self.app = create_app('testing')
#         self.app_context = self.app.app_context()
#         self.app_context.push()
#         self.client = self.app.test_client()

#     def tearDown(self):
#         self.app_context.pop()

#     def test_couch_db_connects_via_FlaskCloudant_extension(self):
#         '''Test that the db object has been created by FlaskCloudant and is not empty'''
#         self.assertIsNotNone(db)
#         # a specific doc in the testing database
#         doc = db.get('0b2f89159bd3602d6448d6ca2b000f68')
#         self.assertIsNotNone(doc)


# class TestFlaskBootstrap(unittest.TestCase):
#     '''Test that FlaskBootstrap extension is present and works'''

#     def setUp(self):
#         '''Creates a version of the Flask application for testing'''
#         self.app = create_app('testing')
#         self.app_context = self.app.app_context()
#         self.app_context.push()
#         self.client = self.app.test_client()

#     def tearDown(self):
#         self.app_context.pop()

#     def test_flask_bootstrap_extension_loads(self):
#         response = self.client.get('/')
#         response_text = response.get_data(as_text=True)
#         self.assertTrue('twitter-bootstrap' in response_text)
#         self.assertTrue('.navbar' in response_text)
