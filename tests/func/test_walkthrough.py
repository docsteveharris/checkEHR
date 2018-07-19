# Functional tests using pytest-selenium


def test_homepage(selenium):
    selenium.get("http://127.0.0.1:5000")
    assert selenium.title == 'checkEHR'
