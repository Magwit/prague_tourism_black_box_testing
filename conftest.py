import pytest
from selenium.webdriver import Chrome

# Fixture to initialize and quit for all tests
@pytest.fixture
def browser(scope='module'):
    print("initiating chrome driver")
    driver = Chrome
    driver.implicitly_wait(10)
    yield driver
    print("quitting chrome driver")
    driver(quit)
