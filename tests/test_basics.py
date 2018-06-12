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
