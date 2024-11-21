# login

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.linkedin.com")
driver.maximize_window()
time.sleep(5)
username = driver.find_element_by_xpath('//*[@id="session_key"]')
username.clear()
username.send_keys("rushikeshjoharkar7@gmail.com")
time.sleep(2)
pw = driver.find_element_by_xpath('//*[@id="session_password"]')
pw.clear()
pw.send_keys("TYGVYJHV")
time.sleep(1)
pw.send_keys(Keys.ENTER)

time.sleep(10)
driver.close()
