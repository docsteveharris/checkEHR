# Functional tests using pytest-selenium
import time


def test_homepage(selenium):
    selenium.get("http://127.0.0.1:5000")
    assert selenium.title == 'checkEHR'


# - [ ] @TODO: (2018-07-19) @resume stop calling browser twice
def test_database_connected(selenium):
    selenium.get("http://127.0.0.1:5000")
    body = selenium.find_element_by_id('database_url')
    time.sleep(2)
    assert 'Database' in body.text
    assert 'testing' in body.text
