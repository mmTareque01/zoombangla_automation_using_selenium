from Locators.locators import Locators
import pytest
from Pages.homePage import Home
from tests.test_base import TestBaseHome
from Others.status import main


class TestHome(TestBaseHome):
    @pytest.mark.home_page
    def test_lunch_using_https(self):
        Home(self.driver).lunch()
        print()
        test_status = self.driver.current_url == Locators.url and self.driver.title == Locators.home_page_title
        # main(self.test_id.get(), "Lunching website using https", test_status)
        assert test_status, "Failed to Lunch HTTPS"
        main(self.test_id.get(), "Lunching website using https", test_status)

    @pytest.mark.home_page
    def test_navigate_to_news(self):
        test_status = Home(self.driver).subdomain_navigation(Locators.news_subdomain_xpat) <= 400
        main(self.test_id.get(), "Navigate to News subdomain", test_status)
        assert test_status, "News paper sub domain is broken"


    @pytest.mark.home_page
    def test_navigate_to_shop(self):
        test_status = Home(self.driver).subdomain_navigation(Locators.shop_subdomain_xpat) <= 400
        main(self.test_id.get(), "Navigate to Shop subdomain", test_status)
        assert test_status, "Shop sub domain is broken"


    @pytest.mark.home_page
    def test_navigate_to_video(self):
        print('Test Id: ', self.test_id.get())
        test_status = Home(self.driver).subdomain_navigation(Locators.video_subdomain_xpat) <= 400
        main(self.test_id.get(), "Navigate to Video subdomain", test_status)
        assert test_status, "Video sub domain is broken"


    @pytest.mark.home_page
    def test_navigate_to_ans(self):
        test_status= Home(self.driver).subdomain_navigation(Locators.answer_subdomain_xpat) <= 400
        main(self.test_id.get(), "Navigate to Answer subdomain", test_status)
        assert test_status, "Answer sub domain is broken"


    @pytest.mark.home_page
    def test_navigate_to_travel(self):
        test_status = Home(self.driver).subdomain_navigation(Locators.travel_subdomain_xpat) <= 400
        main(self.test_id.get(), "Navigate to travel subdomain", test_status)
        assert test_status, "Travel sub domain is broken"


    # @pytest.mark.home_page
    # def navigate_to_news(self):
    #     test_status = Home(self.driver).subdomain_navigation(Locators.news_subdomain_xpat) <= 400
    #     assert test_status, "News paper sub domain is broken"
    #     print(main(self.test_id.get(), "Navigate to News subdomain", test_status))
