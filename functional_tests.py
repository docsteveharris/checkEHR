from selenium import webdriver
import unittest
import time
import pdb


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
        # We see the database name and version displayed
        body = self.browser.find_element_by_id('database_url')
        time.sleep(1)
        self.assertIn('Database', body.text)
        self.assertIn('testing', body.text)


        # I login so that my user id is available for an audit trail
        # - [ ] @TODO: (2018-06-13) @later add in user registration as per
        #   tutorial chapter

        # I see a list of existing validation checks in a table which are
        # identified with a unique code and a snippet
        table = self.browser.find_element_by_tag_name('table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIsNotNone(rows)

        # this contains data from a testing database 
        # the name of the data base and its URL is displayed prominently

        # I click on a row and am taken to a page for that row
        # this page contains a link that allows editing of the data

        # the list is empty at the moment (production only)

        # so I see a link to enter a new validation check in a navigation bar
        # - [ ] @TODO: (2018-06-12) work out selenium and commands
        #   for nav bar
        # self.assertIn('New check', self.browser. ... )

        # I navigate to that link in my browser, and land on a page which
        # identifies itself as 'checkEHR', and as the page where I can enter a
        # new validation check.
        self.fail('progress placeholder: this is where you\' up to ...')

        # I type a correctly a formatted JSON string that contains a list of
        # concept codes, and key:value pairs for context, valid-date,
        # validation check name, and notes.

        # I type enter and the data is saved, and I am re-directed to a page
        # with a list of checks showing a list of  'validation check names',
        # and links back to the data entry page.

        # I repeat the process, and see the list extend by one each time.

        # I click on one of those links and see the JSON displayed.


# if you all this script directly from the command line then run the unit tests
if __name__ == '__main__':
    unittest.main(warnings='ignore')
