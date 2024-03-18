from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

chrome_Driver_path = "C:\\UserCreation_Automation\\webdriver\\chromedriver.exe"
service = Service(chrome_Driver_path)
driver = webdriver.Chrome(service = service)
driver.get("https://www.icc-cricket.com/")
driver.maximize_window()
time.sleep(5)
element = driver.find_element(By.CLASS_NAME, 'si-head')
driver.execute_script("arguments[0].scrollIntoView(true);", element)
time.sleep(5)
print(element.text)
time.sleep(5)


driver.close()