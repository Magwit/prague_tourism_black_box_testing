from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


def test_daytrips_tab_functionality(browser):
    # GIVEN the user is on The Official Tourist website for Prague

    base_url = "https://www.prague.eu/en"

    browser.maximize_window()
    browser.get(base_url)
    try:
        assert "Prague" in browser.title
        print(browser.current_url)
    except AssertionError as e:
        print(e)
        raise e

    # WHEN the user clicks on 'Day Trips' in the navigation bar

    day_trip_nav = "//nav/a[contains(@href, 'trips' )]"

    wait = WebDriverWait(browser, 20)
    try:
        wait.until(EC.element_to_be_clickable((By.XPATH, day_trip_nav)))
    except TimeoutException as e:
        print(e)
        print("------------")
        print(str(e))
        print("------------")
        print(e.args)
        print("============")
    except Exception:
        print("FALLBACK EXCEPTION")

    try:
        day_trip_menu_item = browser.find_element(By.XPATH, day_trip_nav)
        day_trip_menu_item.click()
    except NoSuchElementException as e:
        print(e)
        print("------------")
        print(str(e))
        print("------------")
        print(e.args)
        print("============")
    # THEN the user is on a new tab with information on day trips around Prague

    browser_tabs = browser.window_handles
    size = len(browser_tabs)
    try:
        assert size == 2
    except AssertionError as e:
        print(e)
        raise e

    browser.switch_to.window(browser_tabs[0])
    print(browser.title)

    # Assert that this is the main page
    try:
        assert "Prague" in browser.title
    except AssertionError as e:
        print(e)
        raise e
    browser.switch_to.window(browser_tabs[1])
    print(browser.title)

    # Assert the next tab is the Day Trip page
    try:
        assert "DayTrips" in browser.title
    except AssertionError as e:
        print(e)
        raise e
