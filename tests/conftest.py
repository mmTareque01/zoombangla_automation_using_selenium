import pytest
from Locators.locators import Locators
from configuration.configuration import SeleniumConfiguration
from Others.testId import TestId


@pytest.fixture(scope="module", autouse=True)
def init_driver(request):
    driver = SeleniumConfiguration().Chrome()
    test_id = TestId()
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get(Locators.url)
    request.module.driver = driver
    # request.module.demo = 50
    request.module.test_id = test_id


    yield
    driver.close()
