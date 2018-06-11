import unittest
from app import create_app as tested_app


# now write a unit test that attempts to resolve '/'
class TestURLS(unittest.TestCase):

    def setUp(self):
        '''Creates a version of the Flask application for testing'''
        config_name = 'testing'
        app = tested_app(config_name)
        self.client = app.test_client()

    def tearDown(self):
        pass

    def test_root_url_resolves_to_home_page_view(self):
        ''' Check that the app returns a root URL'''
        result = self.client.get('/')
        assert result.status_code == 200
