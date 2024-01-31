from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class Helper:
    def __init__(self, driver):
        self.driver = driver

    def navigate_to_auto_am(self, url):
        self.driver.get(url)

    def search_car_brand(self, car, locator, options):
        search_input = self.driver.find_element(*locator)
        search_input.send_keys(car)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((options))
        )
        search_options = self.driver.find_element(*options)
        search_options.click()

    def wait_for_search_results(self, locator):
        try:
            results_count_span = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(locator)
            )
            return results_count_span
        except TimeoutException:
            print("Timed out waiting for search results.")
            return None
