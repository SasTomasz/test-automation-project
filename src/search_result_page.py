from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SearchResultPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

        self._search_warning = (By.XPATH, '//div[contains(text(), "search")]')
        self._page_title = (By.XPATH, '//h1[text()="Search"]')

    def check_page_is_ready(self):
        self.wait.until(EC.visibility_of_element_located(self._page_title))

    def get_search_warning(self):
        return self.driver.find_element(*self._search_warning).text