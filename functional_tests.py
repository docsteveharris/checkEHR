from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_enter_json_and_retrieve_it_later(self):
        # A colleague shares a link I can use to access the database.
        self.browser.get('http://localhost:5000')

        # We check the page title is correctly labelled
        self.assertIn('checkEHR', self.browser.title)
        self.fail('do more work, this always fails')

        # I navigate to that link in my browser, and land on a page which
        # identifies itself as 'checkEHR', and as the page where I can enter a
        # new validation check.

        # I type a correctly a formatted JSON string that contains a list of
        # concept codes, and key:value pairs for context, valid-date,
        # validation check name, and notes.

        # I type enter and the data is saved, and I am re-directed to a page
        # with a list of checks showing a list of  'validation check names',
        # and links back to the data entry page.

        # I repeat the process, and see the list extend by one each time.

        # I click on one of those links and see the JSON displayed.


if __name__ == '__main__':
    unittest.main(warnings='ignore')
