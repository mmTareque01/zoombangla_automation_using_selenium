import string
import random
import time
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
        self.driver.get('https://video.zoombangla.com/')
        if self.driver.current_url == 'https://zoombangla.com/#google_vignette':
            self.driver.refresh()
            self.driver.get('https://video.zoombangla.com/')
            assert self.driver.current_url == 'https://video.zoombangla.com/'
        else:
            assert self.driver.current_url == 'https://video.zoombangla.com/'

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
        self.driver.get('https://video.zoombangla.com/?p=169')
        url_before_commenting = self.driver.current_url
        Video(self.driver).post_comment()
        assert url_before_commenting == self.driver.current_url

    @pytest.mark.video_page
    def test_comment_with_invalid_email(self):
        video = Video(self.driver)
        self.driver.get('https://video.zoombangla.com/?p=169')
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
        self.driver.get('https://video.zoombangla.com/?p=169')
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

        # time.sleep(15)

        # using duplicate email
        url_before_commenting = self.driver.current_url
        video.set_name("tester")
        video.set_emial(email)
        video.set_comment("this is comment")
        video.set_website("dddd")
        video.post_comment()
        assert self.driver.current_url != url_before_commenting and self.driver.current_url == Locators.error_comments
