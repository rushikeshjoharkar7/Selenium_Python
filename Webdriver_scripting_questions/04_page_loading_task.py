from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

iterations = 10
total_time_for_all_iterations = 0
for i in range(iterations):
    driver.get("https://mathup.com/games/crossbit")
    time.sleep(2)
    play_button = driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[3]/div[1]')
    play_button.click()
    start_time = time.time()

    difficulty_level = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="__next"]/div[1]/div[1]/div[1]/div/div/div[3]/div/div[1]/p[1]')))
    assert difficulty_level.text.__contains__('Make')
    time.sleep(2)
    end_time = time.time()

    total_time_for_one_iteration = end_time - start_time
    print("Time_for_one_iteration: ", total_time_for_one_iteration)
    total_time_for_all_iterations += total_time_for_one_iteration

average_time = total_time_for_all_iterations / iterations
print("Average_time: ", average_time)

driver.close()