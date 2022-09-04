from Locators.locators import Locators
import pytest
from Pages.homePage import Home
from tests.test_base import TestBaseHome


class TestHome(TestBaseHome):
    @pytest.mark.home_page
    def test_lunch_using_https(self):
        assert self.driver.current_url == Locators.url and self.driver.title == Locators.home_page_title, "Failed to Lunch HTTPS"

    @pytest.mark.home_page
    def test_navigate_to_news(self):
        assert self.homeObj.subdomain_navigation(Locators.news_subdomain_xpat) <= 400, "News paper sub domain is broken"

    @pytest.mark.home_page
    def test_navigate_to_shop(self):
        assert Home(self.driver).subdomain_navigation(Locators.shop_subdomain_xpat) <= 400, "Shop sub domain is broken"

    @pytest.mark.home_page
    def test_navigate_to_video(self):
        assert Home(self.driver).subdomain_navigation(
            Locators.video_subdomain_xpat) <= 400, "Video sub domain is broken"

    @pytest.mark.home_page
    def test_navigate_to_ans(self):
        assert Home(self.driver).subdomain_navigation(
            Locators.answer_subdomain_xpat) <= 400, "Answer sub domain is broken"

    @pytest.mark.home_page
    def test_navigate_to_travel(self):
        assert Home(self.driver).subdomain_navigation(
            Locators.travel_subdomain_xpat) <= 400, "Travel sub domain is broken"

    @pytest.mark.home_page
    def navigate_to_news(self):
        assert Home(self.driver).subdomain_navigation(
            Locators.news_subdomain_xpat) <= 400, "News paper sub domain is broken"
