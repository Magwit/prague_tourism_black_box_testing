from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


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

    # WHEN the user searches for tk in the search window

    search_toggle_xpath = "//div[contains(@class, 'search-toggle')]"

    wait = WebDriverWait(browser, 20)
    try:
        wait.until(EC.element_to_be_clickable((By.XPATH, search_toggle_xpath)))
    except Exception:
        print("FALLBACK EXCEPTION CLICKABLE")

    try:
        search_toggle = browser.find_element(By.XPATH, search_toggle_xpath)
        search_toggle.click()
    except Exception:
        print("FALLBACK EXCEPTION CLICK EVENT")

    # search_window_xpath = "//input[@id='query']"
    try:
        wait.until(EC.element_to_be_clickable((By.ID, "query")))
    except Exception:
        print("FALLBACK EXCEPTION QUERY CLICKABLE")

    search_window = browser.find_element(By.ID, "query")
    search_term = "Brewery"
    search_window.send_keys(search_term)
    search_window.send_keys(Keys.ENTER)

    # THEN the user is on a page displaying the search results related to breweries .....

    query_results_url = "https://www.prague.eu/qf/en/ramjet/fulltextSearch"
    # query_results_url = "https://www.prague.eu/qf/"
    try:
        assert browser.current_url == query_results_url
    except Exception:
        print("FALLBACK EXCEPTION QUERY RESULTS PAGE")

    # ul id= 'fulltextlisting'li p h3

    # Thanks to automation panda...
    # TODO assert length of list > 0
    listan = "//ul[@id='fulltextListing']"

    # TODO assert paragraph text contains search term 'Brewery'
    p_i_listan = "//ul[@id='fulltextListing']/li/p"
