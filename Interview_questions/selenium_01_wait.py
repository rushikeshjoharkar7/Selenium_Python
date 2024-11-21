from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize WebDriver
driver = webdriver.Chrome()

# Set implicit wait for 10 seconds
driver.implicitly_wait(10)

# Navigate to a website
driver.get("https://www.google.com")

# Find the search box (even if it takes up to 10 seconds to load)
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium")
-------------------------------------------------------------------------------

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize WebDriver
driver = webdriver.Chrome()

# Navigate to a website
driver.get("https://www.google.com")

# Explicit wait for the search box to be clickable
wait = WebDriverWait(driver, 10)
search_box = wait.until(EC.element_to_be_clickable((By.NAME, "q")))
search_box.send_keys("Selenium")
