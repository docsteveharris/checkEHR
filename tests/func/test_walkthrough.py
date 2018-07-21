# Functional tests using pytest-selenium
# - [ ] @NOTE: (2018-07-20) following https://github.com/dihnatsyeu
#   /blazemeter-TestNG/blob/master/tests/booking_test.py
import pytest
# from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
# from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures('driver_init')
class BaseTest:
    pass


class TestHomePage(BaseTest):

    # A colleague shares a link I can use to access the database.
    def test_homepage(self):
        WebDriverWait(self.driver, 3)
        self.driver.get("http://127.0.0.1:5000")
    # We check the page title is correctly labelled
        assert self.driver.title == 'checkEHR'

    def test_database_connected(self):
        body = self.driver.find_element_by_id('database_url')
    # We see the database name and version displayed
    # this contains data from a testing database
    # the name of the data base and its URL is displayed prominently
        assert 'Database' in body.text
        assert 'testing' in body.text

    # I login so that my user id is available for an audit trail
    # - [ ] @TODO: (2018-06-13) @later add in user registration as per
    #   tutorial chapter

    # I see a list of existing validation checks in a table which are
    # identified with a unique code and a snippet

    def test_that_table_of_validation_checks_exists(self):
        table = self.driver.find_element_by_tag_name('table')
        rows = table.find_elements_by_tag_name('tr')
        assert rows is not None

    def test_clicking_on_row_in_table_takes_me_to_validation_page(self):
        table = self.driver.find_element_by_tag_name('table')
        rows = table.find_elements_by_tag_name('tr')
        assert len(rows) > 0  # i.e. content plus a header row
        row = rows[1]
        # check that the row is a hyperlink
        html = row.get_attribute('outerHTML')
        assert 'onclick' in html
        assert 'href' in html
        # - [ ] @TODO: (2018-07-21) @resume
        # now check that the link takes to a new page





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
    def progress_placeholder(self):
        self.fail('progress placeholder: this is where you\' up to ...')

    # I type a correctly a formatted JSON string that contains a list of
    # concept codes, and key:value pairs for context, valid-date,
    # validation check name, and notes.

    # I type enter and the data is saved, and I am re-directed to a page
    # with a list of checks showing a list of  'validation check names',
    # and links back to the data entry page.

    # I repeat the process, and see the list extend by one each time.

    # I click on one of those links and see the JSON displayed.