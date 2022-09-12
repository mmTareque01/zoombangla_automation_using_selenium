from Locators.locators import Locators


class Video:
    def __init__(self, driver):
        self.driver = driver

    def video_card_len(self):
        return len(self.driver.find_elements(Locators.video_xpath))

    def load_more_videos(self):
        self.driver.find_element(Locators.load_more_videos_xpath).click()

    def search(self, keyword):
        self.driver.find_element(Locators.video_search_icon_xpath).click()
        self.driver.find_element(Locators.video_search_input_xpath).send_keys(keyword)
        self.driver.find_element(Locators.video_search_button_xpath).click()

    def is_enabled_search_button(self):
        self.driver.find_element(Locators.video_search_icon_xpath).click()
        return self.driver.find_element(Locators.video_search_button_xpath).is_enabled()

    def navigate_to_the_video(self):
        self.driver.find_element(Locators.video_link_xpath).click()

    def set_name(self, author):
        self.driver.find_element(Locators.author_id).send_keys(author)

    def set_emial(self, email):
        self.driver.find_element(Locators.email_id).send_keys(email)

    def set_website(self, url):
        self.driver.find_element(Locators.url_id).send_keys(url)

    def set_comment(self, cmnt):
        self.driver.find_element(Locators.comment_id).send_keys(cmnt)

    def post_comment(self):
        self.driver.find_element(Locators.submit_button_id).click()
