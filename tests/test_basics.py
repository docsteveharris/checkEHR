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
        result = self.client.get('/')
        assert result.status_code == 200
