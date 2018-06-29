# - [ ] @TODO: (2018-06-13) @later @refactor switch to flask pytest layout
# http://flask.pocoo.org/docs/1.0/testing/
import unittest
from flask import current_app
from app import create_app
import requests


# now write a unit test that attempts to resolve '/'
class TestURLS(unittest.TestCase):

    def setUp(self):
        '''Creates a version of the Flask application for testing'''
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()

    def tearDown(self):
        self.app_context.pop()

    def test_app_exists(self):
        '''- As per Example 7-9 in Flask Web Developement'''
        self.assertFalse(current_app is None)

    def test_app_is_testing(self):
        self.assertTrue(current_app.config['TESTING'])

    def test_root_url_resolves_to_home_page_view(self):
        '''Check that the app returns a root URL'''
        response = self.client.get('/')
        assert response.status_code == 200

    def test_home_page_returns_correct_html(self):
        '''
        Aim to replicate Testing a Simple Home Page from the Goat
        '''
        response = self.client.get('/')
        response_text = response.get_data(as_text=True)
        # check for opening and closing HTML tags
        self.assertTrue('<html>' in response_text)
        self.assertTrue('</html>' in response_text)
        # check title corresponds to app
        self.assertTrue('checkEHR' in response_text)


class TestCouchDB(unittest.TestCase):
    '''Test that couchDB is up and running'''

    def setUp(self):
        '''Creates a version of the Flask application for testing'''
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()
        self.host_noauth = 'http://127.0.0.1:5984'
        self.host = 'http://testyMcTestFace:testyMcTestFace@127.0.0.1:5984'

    def tearDown(self):
        self.app_context.pop()

    def test_couchdb_is_version_2plus(self):
        # this occurs manually without using flask-couchdb extension
        # use localhost during testing and dev
        # - [ ] @TODO: (2018-06-19) @later update to correct server
        res = requests.get(self.host_noauth)
        self.assertTrue(200, res.status_code)
        res_json = res.json()
        self.assertTrue('couchdb' in res_json.keys())
        self.assertTrue(res_json['version'], '2.1.1')

    def test_can_login_to_as_testyMcTestFace(self):
        '''Will try and log in without credentials; then test with
        credentials'''
        res = requests.put(self.host_noauth + '/testing_db')
        self.assertTrue(401 == res.status_code)
        # try to delete the database
        try:
            res = requests.delete(self.host + '/testing_db')
            res.raise_for_status()
        except requests.exceptions.HTTPError:
            res = requests.put(self.host + '/testing_db')
            self.assertTrue(201 == res.status_code)


class TestFlaskBootstrap(unittest.TestCase):
    '''Test that FlaskBootstrap extension is present and works'''

    def setUp(self):
        '''Creates a version of the Flask application for testing'''
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()

    def tearDown(self):
        self.app_context.pop()

    def test_flask_bootstrap_extension_loads(self):
        response = self.client.get('/')
        response_text = response.get_data(as_text=True)
        self.assertTrue('twitter-bootstrap' in response_text)
        self.assertTrue('.navbar' in response_text)
