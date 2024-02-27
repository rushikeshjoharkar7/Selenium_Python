import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Specify the version of ChromeDriver that matches your Chrome browser version
chrome_driver_path = "C:\\CHROME_DRIVER_FOLDER_PATH\\chromedriver.exe"

# Initialize Chrome Service
chrome_service = Service(chrome_driver_path)

# Configure Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--ignore-ssl-errors')

# Initialize Chrome WebDriver
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

# Open the desired URL
url = "https://www.google.com"
driver.get(url)
driver.maximize_window()
time.sleep(10)
driver.close()
