from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

chrome_driver_path = "C:\\UserCreation_Automation\\webdriver\\chromedriver.exe"
service = Service(chrome_driver_path)

options = webdriver.ChromeOptions()
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("excludeSwitches", ["enable-automation"])

driver = webdriver.Chrome(service = service, options = options)
driver.get("https://mathup.com/games/crossbit")
driver.maximize_window()
time.sleep(2)

for i in range(10):
    driver.get("https://mathup.com/games/crossbit")
    time.sleep(2)
    play_button = driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[3]/div[1]')
    play_button.click()
    time.sleep(3)

    difficulty_level = driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div[1]/div[1]/div/div/div[5]/div/div[1]/div[2]/div[1]/div[2]/div[2]')
    driver.execute_script("arguments[0].scrollIntoView(true);", difficulty_level)
    print(difficulty_level.text)
    time.sleep(2)

driver.close()