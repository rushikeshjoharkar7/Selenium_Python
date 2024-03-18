from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
a_s_time = time.time()

chrome_driver_path = "C:\\UserCreation_Automation\\webdriver\\chromedriver.exe"
service = Service(chrome_driver_path)

driver = webdriver.Chrome(service = service)

driver.get("https://edition.cnn.com/")
driver.maximize_window()
time.sleep(5)
driver.find_element(By.ID,"onetrust-accept-btn-handler").click()
time.sleep(2)
total_time = 0

for i in range(7):
    st = time.time()
    news_headline = driver.find_element(By.XPATH, '/html/body/div[1]/section[3]/section/div/section/div/div/div/div[2]/div/div[2]/div[1]/div/div[2]/div/div[3]/a/h2')
    print(news_headline.text)
    et = time.time()
    iter_time = et - st
    total_time += iter_time
    print(total_time)
    driver.refresh()
    time.sleep(5)

avg_time = total_time/10
print(avg_time)

a_e_time = time.time()
total_automation_time = a_e_time - a_s_time
print(total_automation_time)
driver.close()
