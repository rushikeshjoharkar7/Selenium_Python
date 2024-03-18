import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def get_element(self, locator_type, locator_value):
        element = None

        if locator_type.endswith("_id"):
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, locator_value)))
        elif locator_type.endswith("_name"):
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, locator_value)))
        elif locator_type.endswith("_link_text"):
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, locator_value)))
        elif locator_type.endswith("_class_name"):
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, locator_value)))
        elif locator_type.endswith("_xpath"):
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, locator_value)))
        elif locator_type.endswith("_css"):
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, locator_value)))

        return element

    def click_on_element(self, locator_type, locator_value):
        element = self.get_element(locator_type, locator_value)
        element.click()

    def enter_text_into_element(self, locator_type, locator_value, text_value):
        element = self.get_element(locator_type, locator_value)
        time.sleep(0.5)
        element.click()
        element.clear()
        element.send_keys(text_value)

    def verify_page_title(self, expected_title):
        return self.driver.title.__eq__(expected_title)

    def verify_error(self, locator_type, locator_value, error_type):
        element = self.get_element(locator_type, locator_value)
        return element.text.__contains__(error_type)

