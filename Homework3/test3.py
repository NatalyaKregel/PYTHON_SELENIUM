from homework3.conftest import testdata
from testpage import OperationsHelper
import logging
import time


def test_step1_negative_login(browser):
    logging.info("Test1 negative starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login("test")
    testpage.enter_pass("test")
    testpage.click_login_btn()
    time.sleep(1)
    assert testpage.get_error_field() == "401", "test negative_login us FAILED!"


def test_step2_positive_login(browser):
    logging.info('Test positive starting')
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(testdata["login"])
    testpage.enter_pass(testdata["pswd"])
    testpage.click_login_btn()
    time.sleep(1)


def test_step3_create_post(browser):
    logging.info('Create new post')
    testpage = OperationsHelper(browser)
    testpage.click_create_btn()
    testpage.title(testdata['title'])
    testpage.description(testdata['description'])
    testpage.content(testdata['content'])
    testpage.click_save_btn()
    time.sleep(1)


def test_step4_filling_form(browser):
    logging.info('Test Starting Homework3')
    testpage = OperationsHelper(browser)
    testpage.click_contact_btn()
    testpage.name(testdata['name'])
    testpage.email(testdata['email'])
    testpage.content_field(testdata['content_field'])
    testpage.click_contact_us_btn()
    time.sleep(1)
    alert = testpage.get_alert_message()
    assert alert == testpage.get_alert_message(), 'Test_positive_form_contact_us FAIL'

