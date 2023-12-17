from selenium.webdriver.chrome.options import Options
import time
from selenium import webdriver

chrome_options = Options()
chrome_options.add_argument("--remote-debugging-port=9222")
chrome_options.add_argument("user-data-dir=C:\\Users\\KloverCloud\\PycharmProjects\\Krack8UIAutomation\\src\\chromedriver\\chromedata")
chrome_driver = "C:\\Users\\KloverCloud\\PycharmProjects\\Krack8UIAutomation\\src\\chromedriver\\chromedriver.exe"

# Remove 'executable_path' argument
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.google.com/')
time.sleep(3)
