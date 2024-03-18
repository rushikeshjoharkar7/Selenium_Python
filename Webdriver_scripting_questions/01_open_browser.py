from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chromedriver_path = "C:\\UserCreation_Automation\\webdriver\\chromedriver.exe"

service = Service(executable_path=chromedriver_path)
options = webdriver.ChromeOptions()
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("excludeSwitches",["enable-automation"])

driver = webdriver.Chrome(service=service, options=options)
driver.maximize_window()
time.sleep(2)
driver.get('https://www.icc-cricket.com/')
time.sleep(5)

accept_button = driver.find_element(By.XPATH, '//button[contains(text(),"Accept All Cookies")]')
accept_button.click()
time.sleep(200)

driver.close()