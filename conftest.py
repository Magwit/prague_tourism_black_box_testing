import pytest
from selenium.webdriver import Chrome

# from selenium.webdriver.support.ui import WebDriverWait

# https://www.guru99.com/pytest-tutorial.html
# Fixture to initialize and quit for all tests
# conftest.py spcefifically allows a pytest fixture to be shared among multiple files
@pytest.fixture
def browser(scope="session"):
    print("initiating chrome driver")
    driver = Chrome()
    # driver.implicitly_wait(5)
    yield driver
    print("quitting chrome driver")
