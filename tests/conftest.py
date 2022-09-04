import pytest
from Locators.locators import Locators
from configuration.configuration import SeleniumConfiguration


@pytest.fixture(scope="class")
def init_driver(request):
    driver = SeleniumConfiguration().Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get(Locators.url)
    request.cls.driver = driver
    yield
    driver.close()
