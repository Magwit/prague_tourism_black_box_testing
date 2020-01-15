from selenium.webdriver import Chrome

# Fixture to initialize and quit for all tests
@pytest.fixture
def browser(scope='module'):
    driver = Chrome
    driver.implicitly_wait(10)
    yield driver
    driver(quit)