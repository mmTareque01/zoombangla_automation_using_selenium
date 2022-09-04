from Pages.contactPage import Contact
from tests.test_base import TestBaseHome
import pytest


class TestContactTest(TestBaseHome):

    @pytest.mark.abc
    def test_lunch_checking(self):
        self.driver.get('https://zoombangla.com/contact-us/')
        if self.driver.current_url == 'https://zoombangla.com/#google_vignette':
            print("ia ma true")
            self.driver.get('https://zoombangla.com/contact-us/')
            assert self.driver.current_url == 'https://zoombangla.com/contact-us/'
        else:
            assert self.driver.current_url == 'https://zoombangla.com/contact-us/'

    @pytest.mark.abc
    def test_checking_google_map(self):
        assert Contact(self.driver).check_google_map()

    # @pytest.mark.abc
    # def test_send_msg_using_valid_data(self):
    #     contact = Contact(self.driver)
    #     contact.set_name("testing")
    #     contact.set_email("tester@gmail.com")
    #     contact.set_subject("this is subject")
    #     contact.set_message("this is demo message")
    #     contact.submit_button_xpath()
    #     assert contact.find_element_using_partial_text(
    #         'Thanks for contacting us! We will be in touch with you shortly.')
