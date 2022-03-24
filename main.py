from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from functionality.sign_in_page import SignIn
from functionality.job_applications import Apply, build_url
from credentials import Credentials as c

s = Service("C:/dev/chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://www.linkedin.com")

page = SignIn(driver)
apply = Apply(driver)
page.sign_in(c.username, c.password)

distance = input("Distance you are willing to drive to go to work?: ")
post = input("For what position would you like to apply?: ")
area = input("Where do you live?: ")

url = build_url(distance, post, area)
driver.get(url)


# apply.apply()

driver.close()

