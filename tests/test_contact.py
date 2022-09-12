import time
from selenium.webdriver.common.by import By
from Pages.contactPage import Contact
# from tests.test_base import TestBaseHome
import pytest


# class TestContactTest(TestBaseHome):

# @pytest.mark.usefixtures("init_driver")
@pytest.mark.abc
def test_lunch_checking(request):

    # print(">>>>>>>>>>>>", request.module.demo)
    # return 1


    drv = request.module.driver
    contactObj = Contact(drv)
    # contactObj.navigate_to()
    contactObj.demo_checking()
    # if '#google_vignette' in drv.current_url:
    #     drv.switch_to.frame('aswift_12')
    #     drv.switch_to.frame('ad_iframe')
    #     drv.find_element(By.XPATH, '//*[@id="dismiss-button"]').click()
    #
    # else:
    #     print("i am from alse")
    #     assert drv.current_url == 'https://zoombangla.com/contact-us/'


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
