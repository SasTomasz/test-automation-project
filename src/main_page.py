from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    def __init__(self, driver: WebDriver):
        self.url = "https://www.ministryoftesting.com/"
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

        self._search_field = (By.ID, "search_query")
        self._search_button = (By.CSS_SELECTOR, "button[aria-label='search']")
        self._sign_in_btn = (By.ID, "nav-sign-in")

    def fill_search_field(self, text):
        self.driver.find_element(*self._search_field).send_keys(text)

    def click_search_button(self):
        self.driver.find_element(*self._search_button).click()

    def go_to_main_page(self):
        self.driver.get(self.url)

    def check_the_page_is_ready(self):
        self.wait.until(EC.visibility_of_element_located(self._sign_in_btn))

