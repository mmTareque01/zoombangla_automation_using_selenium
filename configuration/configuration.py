from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService


class SeleniumConfiguration:

    def Chrome(self):
        return webdriver.Chrome(service=ChromeService("/home/mm/drivers/chromedriver_linux64/chromedriver"))
