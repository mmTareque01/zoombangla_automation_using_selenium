import time

from selenium.webdriver.common.by import By

from Locators.locators import Locators
from Pages.contactPage import Contact
from tests.test_base import TestBaseHome
import pytest


class TestContactTest(TestBaseHome):

    @pytest.mark.abc
    def test_lunch_checking(self):
        drv = self.driver
        contact_obj = Contact(drv)
        contact_obj.navigate_to()
        time.sleep(10)

        if '#google_vignette' in drv.current_url:
            try:
                drv.switch_to.frame(Locators.add_iframe_1)
                drv.switch_to.frame(Locators.add_iframe_2)
                drv.find_element(Locators.add_dismit_button).click()
                assert drv.current_url == 'https://zoombangla.com/contact-us/'
            except:
                self.driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")
                time.sleep(10)
                self.driver.find_element(By.XPATH, Locators.contact_us_xpath).click()
                assert drv.current_url == 'https://zoombangla.com/contact-us/'

        # elif '#google_vignette' in drv.current_url and drv.find_element(By.XPATH, Locators.add_iframe_1) != True:
        #     contact_obj.navigate_to()
        #     assert drv.current_url == 'https://zoombangla.com/contact-us/'
        else:
            assert drv.current_url == 'https://zoombangla.com/contact-us/'

    @pytest.mark.abc
    def test_checking_google_map(self):
        assert Contact(self.driver).check_google_map()

    @pytest.mark.abc
    def test_send_msg_using_valid_data(self):
        contact = Contact(self.driver)
        time.sleep(5)
        contact.set_name("testing")
        contact.set_email("tester@gmail.com")
        contact.set_subject("this is subject")
        contact.set_message("this is demo message")
        contact.submit_form()
        time.sleep(5)
        assert contact.find_confirmation_message()

    @pytest.mark.abc
    def test_send_msg_using_invalid_email(self):
        contact = Contact(self.driver)
        self.driver.refresh()
        time.sleep(5)
        contact.set_name("testing")
        contact.set_email("tester.com")
        contact.set_subject("this is subject")
        contact.set_message("this is demo message")
        contact.submit_form()
        time.sleep(5)
        assert contact.get_input_error('wpforms-1542-field_1-error')

    @pytest.mark.abc
    def test_send_msg_without_required_data(self):
        contact = Contact(self.driver)
        self.driver.refresh()
        time.sleep(5)
        contact.submit_form()
        assert contact.get_input_error('wpforms-1542-field_1-error') and contact.get_input_error(
            'wpforms-1542-field_0-error') and contact.get_input_error('wpforms-1542-field_2-error')
