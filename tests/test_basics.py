import unittest
from app import create_app as tested_app


# class SmokeTest(unittest.TestCase):
#     '''
#     a test that must always fail (to check the testing system works!)
#     '''
#     def test_bad_maths(self):
#         self.assertEqual(1 + 1, 3)


# now write a unit test that attempts to resolve '/'
class TestURLS(unittest.TestCase):

    def setUp(self):

        app = tested_app()
        self.client = app.test_client()

    def tearDown(self):
        pass

    def test_home_url_resolves(self):
        ''' Check that the app returns a root URL'''
        result = self.client.get('/')
        assert result.status_code == 200
