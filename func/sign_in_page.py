from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from locators.sign_in_locators import Locators


class SignIn:

    def __init__(self, browser):
        self.browser = browser

    def enter_username(self, username):
        username_field = self.browser.find_element(By.NAME, Locators.EMAIL_OR_PHONE)
        username_field.send_keys(username)

    def enter_password(self, password):
        password_field = self.browser.find_element(By.NAME, Locators.PASSWORD)
        password_field.send_keys(password)

    def click_sign_in(self):
        button = self.browser.find_element(By.CLASS_NAME, Locators.SIGN_IN_BUTTON)
        button.click()

    def sign_in(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_sign_in()








