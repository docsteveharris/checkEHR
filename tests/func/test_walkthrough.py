# Functional tests using pytest-selenium
# - [ ] @NOTE: (2018-07-20) following https://github.com/dihnatsyeu
#   /blazemeter-TestNG/blob/master/tests/booking_test.py
import pytest
# from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
import time


@pytest.mark.usefixtures('driver_init')
class BaseTest:
    pass


class TestHomePage(BaseTest):

    def test_homepage(self):
        wait = WebDriverWait(self.driver, 3)
        self.driver.get("http://127.0.0.1:5000")
        assert self.driver.title == 'checkEHR'

    def test_database_connected(self):
        self.driver.get("http://127.0.0.1:5000")
        body = self.driver.find_element_by_id('database_url')
        time.sleep(2)
        assert 'Database' in body.text
        assert 'testing' in body.text
