import pytest
from src.driver_factory import DriverFactory
from src.main_page import MainPage


@pytest.fixture
def driver():
    driver = DriverFactory.get_driver('chrome')
    yield driver
    driver.quit()

@pytest.fixture
def main_page(driver):
    main_page = MainPage(driver)
    return main_page