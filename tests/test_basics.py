# - [ ] @TODO: (2018-06-13) @later @refactor switch to flask pytest layout
# http://flask.pocoo.org/docs/1.0/testing/
import unittest
from flask import current_app
from app import create_app


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

    def test_couchdb_is_version_2plus(self):
        import urllib.request
        import json
        # use localhost during testing and dev
        # - [ ] @TODO: (2018-06-19) @later update to correct server
        response = urllib.request.urlopen('http://127.0.0.1:5984')
        self.assertTrue(200, response.status)
        response_dict = json.loads(response.read())
        self.assertTrue('couchdb' in response_dict.keys())
        self.assertTrue(response_dict['version'], '2.1.1')


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
