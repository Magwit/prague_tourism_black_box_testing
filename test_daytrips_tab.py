from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_daytrips_tab_functionality(browser):
    # GIVEN the user is on The Official Tourist website for Prague
    base_url = "https://www.prague.eu/en"

    browser.maximize_window()
    browser.get(base_url)
    assert "Prague" in browser.title

    # WHEN the user clicks on 'Day Trips' in the top menu
    wait = WebDriverWait(browser, 20)
    wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Day Trips")))
    day_trip_menu_item = browser.find_element(By.LINK_TEXT, "Day Trips")
    day_trip_menu_item.click()

    # THEN the user is on a new tab with information on day trips around Prague
    # Different selenium problem is to assert that the day trip tab is the active window
