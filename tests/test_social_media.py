from Pages.homePage import Home
from Locators.locators import Locators
from tests.test_base import TestBaseHome
import pytest


class TestSocialMedia(TestBaseHome):

    @pytest.mark.social_media
    def test_check_facebook(self):
        assert Home(self.driver).check_social_media(Locators.facebook) == 302

    @pytest.mark.social_media
    def test_check_instagram(self):
        assert Home(self.driver).check_social_media(Locators.instagram) == 200

    @pytest.mark.social_media
    def test_check_twitter(self):
        assert Home(self.driver).check_social_media(Locators.twitter) == 200

    @pytest.mark.social_media
    def test_check_youtube(self):
        assert Home(self.driver).check_social_media(Locators.youtube) == 301
