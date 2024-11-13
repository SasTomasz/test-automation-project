import pytest
from src.driver_factory import DriverFactory

@pytest.fixture
def driver():
    driver = DriverFactory.get_driver('chrome')
    yield driver
    driver.quit()
