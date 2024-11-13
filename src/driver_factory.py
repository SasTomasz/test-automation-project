from selenium.webdriver.chrome.webdriver import WebDriver as ChromeWebDriver
from selenium.webdriver.edge.webdriver import WebDriver as EdgeWebDriver
from selenium.webdriver.firefox.webdriver import WebDriver as FirefoxWebDriver


class DriverFactory:
    @staticmethod
    def get_driver(browser_name):

        if browser_name == 'chrome':
            driver = ChromeWebDriver()
        elif browser_name == 'firefox':
            driver = FirefoxWebDriver()
        elif browser_name == 'edge':
            driver = EdgeWebDriver()
        else:
            raise ValueError(f"Browser {browser_name} is not supported")

        driver.set_window_size(1920, 1080)
        return driver
