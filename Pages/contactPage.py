from selenium.webdriver.common.by import By
from Locators.locators import Locators


class Contact:
    def __init__(self, driver):
        self.driver = driver
        self.name_input_field_xpath = Locators.name_input_field_xpath
        self.email_input_field_xpath = Locators.email_input_field_xpath
        self.subject_input_field_xpath = Locators.subject_input_field_xpath
        self.message_field_xpath = Locators.message_input_field_xpath
        self.submit_button_xpath = Locators.submit_button_xpath
        self.map_xpath = '/html/body/div[2]/div[4]/div/div[1]/div/div/div/div[4]/div/div[2]/section/div/div[2]'
        self.contact_us_page_xpath = '//*[@id="wpforms-submit-1542"]'

    def navigate_to(self):
        # self.driver.
        self.driver.find_element(By.XPATH, self.contact_us_page_xpath).click()

    def check_url(self):
        return self.driver.current_url

    def check_google_map(self):
        return self.driver.find_element(By.XPATH, self.map_xpath).is_displayed()

    def set_name(self, name):
        self.driver.find_element(By.XPATH, self.name_input_field_xpath).send_keys(name)
        # return 1

    def set_email(self, email):
        self.driver.find_element(By.XPATH, self.email_input_field_xpath).send_keys(email)
        # return 1

    def set_subject(self, sub):
        self.driver.find_element(By.XPATH, self.subject_input_field_xpath).send_keys(sub)
        # return 1

    def set_message(self, msg):
        self.driver.find_element(By.XPATH, Locators.message_input_field_xpath).send_keys(msg)
        # return 1

    def submit_form(self):
        self.driver.find_element(By.ID, "wpforms-submit-1542").click()
        # return

    def find_element_using_partial_text(self, text):
        return self.driver.find_element(By.PARTIAL_LINK_TEXT, text)
