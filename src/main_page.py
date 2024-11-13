from selenium.webdriver.common.by import By

class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self._search_field = (By.ID, "search_query")
        self._search_button = (By.CSS_SELECTOR, "button[aria-label='search']")
        self._sign_in_btn = (By.ID, "nav-sign-in")

    def fill_search_field(self, text):
        pass

    def click_search_button(self):
        pass

    def go_to_main_page(self):
        pass

    def check_the_page_is_ready(self):
        pass

