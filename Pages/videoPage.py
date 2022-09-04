from Locators.locators import Locators
from selenium.webdriver.common.by import By


class Video:
    def __init__(self, driver):
        self.driver = driver

    def video_card_len(self):
        return len(self.driver.find_elements(By.XPATH, Locators.video_xpath))

    def load_more_videos(self):
        self.driver.find_element(By.XPATH, Locators.load_more_videos_xpath).click()

    def search(self, keyword):
        self.driver.find_element(By.XPATH, Locators.video_search_icon_xpath).click()
        self.driver.find_element(By.XPATH, Locators.video_search_input_xpath).send_keys(keyword)
        self.driver.find_element(By.XPATH, Locators.video_search_button_xpath).click()

    def is_enabled_search_button(self):
        self.driver.find_element(By.XPATH, Locators.video_search_icon_xpath).click()
        return self.driver.find_element(By.XPATH, Locators.video_search_button_xpath).is_enabled()

    def navigate_to_the_video(self):
        self.driver.find_element(By.XPATH, Locators.video_link_xpath).click()

    def set_name(self, author):
        self.driver.find_element(By.ID, "author").send_keys(author)

    def set_emial(self, email):
        self.driver.find_element(By.ID, "email").send_keys(email)

    def set_website(self, url):
        self.driver.find_element(By.ID, "url").send_keys(url)

    def set_comment(self, cmnt):
        self.driver.find_element(By.ID, "comment").send_keys(cmnt)

    def post_comment(self):
        self.driver.find_element(By.ID, "submit").click()
