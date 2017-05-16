from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from functional_tests.base import Page


class HomePage(Page):
    home_page_container = (By.CSS_SELECTOR, ".home-page")

    def __init__(self, driver, relative_url='/'):
        super(HomePage, self).__init__(driver, '/')

    def wait_for_loading(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(lambda driver: driver.find_element(*self.home_page_container))
        return self
