import requests
from selenium.webdriver.common.by import By
from Locators.locators import Locators


class Home:
    def __init__(self, driver):
        self.driver = driver
        self.search_icon_xpath = Locators.search_icon_xpath
        self.search_box_xpath = Locators.search_box_xpath
        self.seacrh_button_xpath = Locators.seacrh_button_xpath

    def lunch(self, url=Locators.url):
        self.driver.get(url)

    def search(self, keyword):
        self.driver.find_element(By.XPATH, self.search_icon_xpath).send_keys(keyword)
        self.driver.find_element(By.XPATH, self.search_box_xpath).send_keys(keyword)
        self.driver.find_element(By.XPATH, self.seacrh_button_xpath).click()

    def subdomain_navigation(self, path):
        link = self.driver.find_element(By.XPATH, path).get_attribute('href')
        return requests.head(link).status_code

    def navigate_to(self, path):
        self.driver.find_element(By.XPATH, path).click()

    def check_social_media(self, path):
        link = self.driver.find_element(By.XPATH, path).get_attribute('href')
        return requests.head(link).status_code
