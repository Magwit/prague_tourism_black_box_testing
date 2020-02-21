from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException, NoSuchElementException


def test_search_bar_functionality(browser):
    # GIVEN the user is on the officiaL tourist websire for Prague

    base_url = "https://www.prague.eu/en"

    browser.maximize_window()
    browser.get(base_url)

    # WHEN the user searches for 'Brewery' in the search window

    search_toggle_xpath = "//div[contains(@class, 'search-toggle')]"

    wait = WebDriverWait(browser, 20)
    try:
        wait.until(EC.element_to_be_clickable((By.XPATH, search_toggle_xpath)))
    except TimeoutException as e:
        print(e)
        raise (e)
    except Exception as e:
        print(e)
        raise e

    try:
        search_toggle = browser.find_element(By.XPATH, search_toggle_xpath)
        search_toggle.click()
    except NoSuchElementException as e:
        print(e)
        raise e
    except Exception as e:
        print(e)
        raise e

    # search_window clickable
    try:
        wait.until(EC.element_to_be_clickable((By.ID, "query")))
    except TimeoutException as e:
        print(e)
        raise e
    except Exception as e:
        print(e)
        raise e

    search_window = browser.find_element(By.ID, "query")
    search_term = "Brewery"
    search_window.send_keys(search_term)
    search_window.send_keys(Keys.ENTER)

    # THEN the user is on a page that displays
    # the search results related to breweries

    query_results_url = "https://www.prague.eu/qf/en/ramjet/fulltextSearch"

    # Assert correct url

    try:
        assert browser.current_url == query_results_url
    except AssertionError as e:
        print(e)
        raise e
    except Exception as e:
        print(e)
        raise e

    # Assert that the list for results is visible
    full_text_list_xpath = "//ul[@id='fulltextListing']"
    try:
        wait.until(EC.visibility_of_element_located((By.XPATH, full_text_list_xpath)))
    except TimeoutException as e:
        print(e)
        raise e
    except Exception as e:
        print(e)
        raise e

    results_xpath = (
        f"//ul[@id='fulltextListing']/li//*[contains(text(), '{search_term}')]"
    )
    # Assert both that a results list exists
    # and that the search term is found in the result list
    try:
        results = browser.find_elements(By.XPATH, results_xpath)
        assert len(results) > 0
    except AssertionError as e:
        print(e)
        raise e
