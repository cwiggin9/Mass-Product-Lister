from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from fake_useragent import UserAgent
from selenium.webdriver.common.by import By
import time
import random

email = "email"
password = "password"

chrome_options = Options()
ua = UserAgent()
userAgent = ua.random
chrome_options.add_argument(f'user-agent={userAgent}')
chrome_options.add_argument("--incognito")
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.get("https://www.redbubble.com/auth/login")

def human_type(element, text):
    for char in text:
        time.sleep(round(random.uniform(0.00, 0.33), 2))
        element.send_keys(char)

human_type(driver.find_element(By.NAME, "cognitoUsername"),email)
time.sleep(2)
human_type(driver.find_element(By.NAME, "password"),password)
time.sleep(2)
driver.find_element(By.CLASS_NAME, "app-ui-components-Button-Button_button_1_MpP").click()

print("logged in successfully")