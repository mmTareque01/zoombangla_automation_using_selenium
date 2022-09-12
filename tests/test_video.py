import string
import random
import time

from selenium.webdriver.common.by import By

from Pages.videoPage import Video
from Locators.locators import Locators
from tests.test_base import TestBaseHome
import pytest


class TestVideos(TestBaseHome):
    def generateEmail(self):
        name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
        return (name + "@" + "email.com")

    @pytest.mark.video_page
    def test_lunch_video(self):
        drv = self.driver
        video_obj = Video(drv)
        time.sleep(10)
        video_obj.navigate_to_video()
        if '#google_vignette' in drv.current_url:
            time.sleep(5)
            drv.switch_to.frame(Locators.add_iframe_1)
            drv.switch_to.frame(Locators.add_iframe_2)
            drv.find_element(By.XPATH, Locators.add_dismiss_button).click()
            time.sleep(10)
            assert drv.current_url == 'https://video.zoombangla.com/'
        else:
            assert drv.current_url == 'https://video.zoombangla.com/'

    @pytest.mark.video_page
    def test_check_video(self):
        assert Video(self.driver).video_card_len() > 0

    @pytest.mark.video_page
    def test_load_more_videos(self):
        crnt_len = Video(self.driver).video_card_len()
        Video(self.driver).load_more_videos()
        assert Video(self.driver).video_card_len() >= crnt_len

    @pytest.mark.video_page
    def test_search_using_valid_keyword(self):
        keyword = 'a'
        Video(self.driver).search(keyword)
        assert self.driver.current_url == 'https://video.zoombangla.com/?s=' + keyword

    @pytest.mark.video_page
    def test_search_without_keyword(self):
        self.driver.back()
        assert not Video(self.driver).is_enabled_search_button()

    @pytest.mark.video_page
    def test_comment_using_valid_data(self):
        video = Video(self.driver)
        video.navigate_to_the_video()
        url_before_commenting = self.driver.current_url
        video.set_name("tester")
        video.set_emial(self.generateEmail())
        video.set_comment("this is comment")
        video.set_website("dddd")
        video.post_comment()
        assert self.driver.current_url != url_before_commenting and self.driver.current_url != Locators.error_comments

    @pytest.mark.video_page
    def test_comment_without_data(self):
        video = Video(self.driver)
        self.driver.get('https://video.zoombangla.com/?p=140')
        url_before_commenting = self.driver.current_url
        video.post_comment()
        assert url_before_commenting == self.driver.current_url

    @pytest.mark.video_page
    def test_comment_with_invalid_email(self):
        video = Video(self.driver)
        self.driver.get('https://video.zoombangla.com/?p=140')
        url_before_commenting = self.driver.current_url
        video.set_name("tester")
        video.set_emial("email")
        video.set_comment("this is comment using invalid email")
        video.set_website("dddd")
        video.post_comment()
        assert url_before_commenting == self.driver.current_url

    @pytest.mark.video_page
    def test_comment_using_duplicate_email(self):
        video = Video(self.driver)
        self.driver.get('https://video.zoombangla.com/?p=140')
        email = self.generateEmail()
        # first comment
        time.sleep(30)
        video.set_name("tester")
        video.set_emial(email)
        # time.sleep(15)
        video.set_comment("this is comment")
        # time.sleep(15)
        video.set_website("dddd")
        video.post_comment()

        # using duplicate email
        url_before_commenting = self.driver.current_url
        video.set_name("tester")
        video.set_emial(email)
        video.set_comment("this is comment")
        video.set_website("dddd")
        video.post_comment()
        assert self.driver.current_url == Locators.error_comments
