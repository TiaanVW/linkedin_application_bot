from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from func.sign_in_page import SignIn
from credentials import Credentials as c

s = Service("C:/dev/chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://www.linkedin.com")
page = SignIn(driver)

page.sign_in(c.username, c.password)

driver.close()


