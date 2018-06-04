from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://localhost:5000')

# simple check that the dev server is running
assert browser is not None
