import time

from selenium.webdriver.common.by import By

from locators.apply_locators import Locators


def build_url(distance, post, location):
    url = f"https://www.linkedin.com/jobs/search/?distance={distance}&keywords={post}&location={location}"
    return url


class Apply:

    def __init__(self, browser):
        self.browser = browser

    def enter_phone_num(self, phone_number):
        text_box = self.browser.find_element(By.ID, Locators.PHONE_NUM_LOCATOR)
        text_box.send_keys(phone_number)

    def find_apply_now(self):
        apply_now_button = self.browser.find_element(By.ID, Locators.APPLY_NOW_LOCATOR)
        if apply_now_button:
            return True
        else:
            return False

    def click_apply_now(self):
        apply_now_button = self.browser.find_element(By.ID, Locators.APPLY_NOW_LOCATOR)
        apply_now_button.click()

    def locate_submit(self):
        submit_button = self.browser.find_element(By.ID, Locators.APPLY_BUTTON_LOCATOR)
        if submit_button:
            return True

    def click_submit(self):
        submit_button = self.browser.find_element(By.ID, Locators.APPLY_BUTTON_LOCATOR)
        submit_button.click()

    # def apply(self):
    #     job_cards_container = self.browser.find_elements(By.CLASS_NAME, Locators.JOB_CARD_LOCATOR)
    #     for li in job_cards_container:
    #         time.sleep(2)
