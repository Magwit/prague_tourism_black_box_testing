# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC


def test_search_bar_functionality(browser):
    # GIVEN the user is on the officiaL tourist websire for Prague

    base_url = "https://www.prague.eu/en"

    browser.maximize_window()
    browser.get(base_url)
    # TODO continue without considering the conftest thing.
    # Next project there are other goals and one day
    # that goal will adress the very problem I face now.
    # hastag GoodEnough
    pass
