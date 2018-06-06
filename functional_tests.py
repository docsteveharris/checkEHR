from selenium import webdriver

browser = webdriver.Firefox()

# A colleague shares a link I can use to access the database.
browser.get('http://localhost:5000')


# I navigate to that link in my browser, and land on a page which identifies
# itself as 'checkEHR', and as the page where I can enter a new validation
# check.
assert 'checkEHR' in browser.title

# I type a correctly a formatted JSON string that contains a list of concept
# codes, and key:value pairs for context, valid-date, validation check name,
# and notes.

# I type enter and the data is saved, and I am re-directed to a page with a
# list of checks showing a list of  'validation check names', and links back
# to the data entry page.

# I repeat the process, and see the list extend by one each time.

# I click on one of those links and see the JSON displayed.

