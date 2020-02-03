from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_daytrips_tab_functionality(browser):
    # GIVEN the user is on The Official Tourist website for Prague

    base_url = "https://www.prague.eu/en"

    browser.maximize_window()
    browser.get(base_url)
    assert "Prague" in browser.title
    print(browser.current_url)

    # WHEN the user clicks on 'Day Trips' in the top menu

    wait = WebDriverWait(browser, 20)
    wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Day Trips")))
    day_trip_menu_item = browser.find_element(By.LINK_TEXT, "Day Trips")
    day_trip_menu_item.click()
    # TODO look into try expect

    # THEN the user is on a new tab with information on day trips around Prague

    # https://www.browserstack.com/guide/python-selenium-to-run-web-automation-test
    # http://allselenium.info/handling-multiple-windows-python-selenium/
    browser_tabs = browser.window_handles
    size = len(browser_tabs)
    assert size == 2
    # assert "Prague" in browser_tabs[1]
    # for x in range(size):

    #     browser.switch_to.window(browser_tabs[x])
    #     print(browser.title)

    browser.switch_to.window(browser_tabs[0])
    print(browser.title)
    assert "Prague" in browser.title
    browser.switch_to.window(browser_tabs[1])
    print(browser.title)
    assert "DayTrips" in browser.title
