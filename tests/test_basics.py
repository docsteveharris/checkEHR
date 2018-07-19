# - [ ] @TODO: (2018-06-13) @resume @refactor switch to flask pytest layout
# # http://flask.pocoo.org/docs/1.0/testing/
from flask import url_for, g, Flask
from app import db
import pytest
import requests


def test_foo():
    pass


def test_pytest_flask_app(app):
    '''Check the pytest-flask extension has generated an app via the fixture
    declared in conftest.py'''
    assert isinstance(app, Flask)


@pytest.mark.usefixtures('client_class', 'config')
class TestBasics:


    def test_index(self):
        g.db = db
        res = self.client.get(url_for('main.index'))
        assert res.status_code == 200

    def test_app_is_testing(self):
        assert self.client.application.config['TESTING'] is True

    def test_home_page_returns_correct_html(self):
        '''
        Aim to replicate Testing a Simple Home Page from the Goat
        '''
        g.db = db
        res = self.client.get('/').get_data(as_text=True)
        assert '<html>' in res
        assert '</html>' in res
        # check title corresponds to app
        assert 'checkEHR' in res


# import unittest
# from flask import current_app
# from app import create_app, db
# import requests


# class TestCouchDB():
#     '''Test CouchDB independently of Flask'''

#     host_noauth = 'http://127.0.0.1:5984'

#     # def setUp(self):
#     #     '''Creates a version of the Flask application for testing'''
#     #     self.host = 'http://testyMcTestFace:testyMcTestFace@127.0.0.1:5984'

#     def test_couchdb_is_version_2plus(host_noauth):
#         # this occurs manually without using flask-couchdb extension
#         # use localhost during testing and dev
#         # - [ ] @TODO: (2018-06-19) @later update to correct server
#         res = requests.get(host_noauth)
#         assert res.status_code == 200




# class TestCouchDB(unittest.TestCase):
#     '''Test that couchDB is up and running'''

#     def setUp(self):
#         '''Creates a version of the Flask application for testing'''
#         self.app = create_app('testing')
#         self.app_context = self.app.app_context()
#         self.app_context.push()
#         self.client = self.app.test_client()
#         self.host_noauth = 'http://127.0.0.1:5984'
#         self.host = 'http://testyMcTestFace:testyMcTestFace@127.0.0.1:5984'

#     def tearDown(self):
#         self.app_context.pop()

#     def test_couchdb_is_version_2plus(self):
#         # this occurs manually without using flask-couchdb extension
#         # use localhost during testing and dev
#         # - [ ] @TODO: (2018-06-19) @later update to correct server
#         res = requests.get(self.host_noauth)
#         self.assertTrue(200, res.status_code)
#         res_json = res.json()
#         self.assertTrue('couchdb' in res_json.keys())
#         self.assertTrue(res_json['version'], '2.1.1')

#     def test_can_login_to_as_testyMcTestFace(self):
#         '''Will try and log in without credentials; then test with
#         credentials'''
#         res = requests.put(self.host_noauth + '/testing_db_via_requests')
#         self.assertTrue(401 == res.status_code)
#         # try to delete the database
#         try:
#             res = requests.delete(self.host + '/testing_db_via_requests')
#             res.raise_for_status()
#         except requests.exceptions.HTTPError:
#             res = requests.put(self.host + '/testing_db_via_requests')
#             self.assertTrue(201 == res.status_code)
#         finally:
#             requests.delete(self.host + '/testing_db_via_requests')

#     def test_cloudant_api_works(self):
#         '''Try connection with cloudant API rather than requests'''
#         from cloudant import couchdb
#         with couchdb(
#                 'testyMcTestFace',
#                 'testyMcTestFace',
#                 url=self.host_noauth) as client:
#             self.assertIsNotNone(client.all_dbs())
#             db = client.create_database('testing_db_via_cloudant')
#             self.assertTrue('testing_db_via_cloudant' in client.all_dbs())
#             self.assertTrue(db.exists())
#             client.delete_database('testing_db_via_cloudant')
#             # session = client.session()
#             # import pdb; pdb.set_trace()
#             # print(session.all_dbs())

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
