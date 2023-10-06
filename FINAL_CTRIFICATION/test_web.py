from time import sleep
import yaml
from testpage import OperationsHelper
import logging

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)


def test_login_negative(browser):
    logging.info("Test login_negative Starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(testdata['login_invalid'])
    testpage.enter_pass(testdata['pswd_invalid'])
    testpage.click_login_button()
    assert testpage.get_error_text() == "401", "test login negative FAILED"


def test_login_positive(browser):
    logging.info("Test login_positive Starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(testdata['login'])
    testpage.enter_pass(testdata['pswd'])
    testpage.click_login_button()
    assert testpage.login_success() == f"Hello, {testdata['login']}", "test login positive FAILED"


def test_title_page_about(browser, finding_about):
    logging.info("Test display page title Starting")
    testpage = OperationsHelper(browser)
    testpage.click_about_button()
    sleep(1)
    assert testpage.title_page_about() == finding_about, "test title page about FAILED!"


def test_font_size(browser, about_font):
    logging.info("Test font size Starting")
    testpage = OperationsHelper(browser)
    sleep(1)
    received_font = testpage.title_font()
    assert received_font == about_font, logging.exception("test font size title about FAILED!")


