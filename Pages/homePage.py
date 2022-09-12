import requests
from selenium.webdriver.common.by import By
from Locators.locators import Locators


class Home:
    def __init__(self, driver):
        self.driver = driver

    def lunch(self, url=Locators.url):
        self.driver.get(url)

    def search(self, keyword):
        self.driver.find_element(Locators.search_icon_home_page).send_keys(keyword)
        self.driver.find_element(Locators.search_box_xpath).send_keys(keyword)
        self.driver.find_element(Locators.seacrh_button_xpath).click()

    def subdomain_navigation(self, path):
        link = self.driver.find_element(By.XPATH, path).get_attribute('href')
        return requests.head(link).status_code

    def navigate_to(self, path):
        self.driver.find_element(By.XPATH, path).click()

    def check_social_media(self, path):
        link = self.driver.find_element(By.XPATH, path).get_attribute('href')
        return requests.head(link).status_code
