import time

from selenium.webdriver.common.by import By
from Locators.locators import Locators


class Contact:
    def __init__(self, driver):
        self.driver = driver
        self.contact_us_page_xpath = '//*[@id="wpforms-submit-1542"]'

    def navigate_to(self):
        time.sleep(10)

        try:
            self.driver.find_element(Locators.contact_us_xpath).click()

        except:
            self.driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")
            # self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(Locators.contact_us_xpath))
            time.sleep(10)
            self.driver.find_element(Locators.contact_us_xpath).click()

    def check_url(self):
        return self.driver.current_url

    def demo_checking(self):
        print("hello world")

    def check_google_map(self):
        return self.driver.find_element(Locators.map_xpath).is_displayed()

    def set_name(self, name):
        self.driver.find_element(Locators.name_input_field_xpath).send_keys(name)
        # return 1

    def set_email(self, email):
        self.driver.find_element(Locators.email_input_field_xpath).send_keys(email)
        # return 1

    def set_subject(self, sub):
        self.driver.find_element(Locators.subject_input_field_xpath).send_keys(sub)
        # return 1

    def set_message(self, msg):
        self.driver.find_element(Locators.message_input_field_xpath).send_keys(msg)
        # return 1

    def submit_form(self):
        self.driver.find_element(Locators.submit_button).click()
        # return

    def get_input_error(self, id):
        return self.driver.find_element(By.ID, id).is_displayed()

    def find_confirmation_message(self):
        return self.driver.find_element(Locators.form_submit_confirmation_button).is_displayed()

    def close_add(self):
        self.driver.switch_to.frame('ad_iframe')
        self.driver.find_element(By.XPATH, '//*[@id="dismiss-button"]').click
        self.driver.switch_to.default_content()
