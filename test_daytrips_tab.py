def test_daytrips_tab_functionality(browser):
    # GIVEN the user is on The Official Tourist website for Prague
    base_url = "https://www.prague.eu/en"

    browser.maximize_window()
    browser.get(base_url)
    assert "Prague" in browser.title
    # WHEN the userclicks on 'Day Trips' in the top menu

    # THEN the user is on a new tab with information on day trips around Prague
