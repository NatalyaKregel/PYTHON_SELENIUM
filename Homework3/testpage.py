import time
from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging


class TestSearchLocators:
    LOCATOR_LOGIN_FIELD = (By.XPATH, """//*[@id="login"]/div[1]/label/input""")
    LOCATOR_PASS_FIELD = (By.XPATH, """//*[@id="login"]/div[2]/label/input""")
    LOCATOR_LOGIN_BTN = (By.CSS_SELECTOR, "button")
    LOCATOR_ERROR_FIELD = (By.XPATH, """//*[@id="app"]/main/div/div/div[2]/h2""")

    LOCATOR_CREATE_POST_BTN = (By.CSS_SELECTOR, """#create-btn""")
    LOCATOR_TITLE = (By.XPATH, """//*[@id="create-item"]/div/div/div[1]/div/label/input""")
    LOCATOR_DESCRIPTION = (By.XPATH, """//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea""")
    LOCATOR_CONTENT = (By.XPATH, """//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea""")
    LOCATOR_SAVE_BTN = (By.XPATH, """//*[@id="create-item"]/div/div/div[7]/div/button""")

    LOCATOR_CONTACT_BTN = (By.CSS_SELECTOR, """#app>main>nav>ul>li:nth-child(2)>a""")
    LOCATOR_NAME_FIELD = (By.XPATH, """//*[@id="contact"]/div[1]/label/input""")
    LOCATOR_EMAIL_FIELD = (By.XPATH, """//*[@id="contact"]/div[2]/label/input""")
    LOCATOR_CONTENT_FIELD = (By.XPATH, """//*[@id="contact"]/div[3]/label/span/textarea""")
    LOCATOR_CONTACT_US_BTN = (By.XPATH, """//*[@id="contact"]/div[4]/button/span""")


class OperationsHelper(BasePage):
    # _____________enter account_____________________________________________________________
    def enter_login(self, word):
        logging.info(f"Send '{word}' to element {TestSearchLocators.LOCATOR_LOGIN_FIELD[1]}")
        enter_login = self.find_element(TestSearchLocators.LOCATOR_LOGIN_FIELD)
        enter_login.clear()
        enter_login.send_keys(word)

    def enter_pass(self, word):
        logging.info(f"Send '{word}' to element {TestSearchLocators.LOCATOR_PASS_FIELD[1]}")
        enter_pass = self.find_element(TestSearchLocators.LOCATOR_PASS_FIELD)
        enter_pass.clear()
        enter_pass.send_keys(word)

    def click_login_btn(self):
        logging.info("Click login button")
        self.find_element(TestSearchLocators.LOCATOR_LOGIN_BTN).click()

    def get_error_field(self):
        logging.info(f"Start find error text")
        error_field = self.find_element(TestSearchLocators.LOCATOR_ERROR_FIELD, time=2)
        text = error_field.text
        logging.info(f"We find text '{text}' in error field {TestSearchLocators.LOCATOR_ERROR_FIELD[1]}")
        return text

    # ______________create new post___________________________________________________________

    def click_create_btn(self):
        logging.info("Click create button")
        self.find_element(TestSearchLocators.LOCATOR_CREATE_POST_BTN).click()

    def title(self, word):
        logging.info(f"Send '{word}' to element {TestSearchLocators.LOCATOR_TITLE[1]}")
        title = self.find_element(TestSearchLocators.LOCATOR_TITLE)
        title.clear()
        title.send_keys(word)

    def description(self, word):
        logging.info(f"Send '{word}' to element {TestSearchLocators.LOCATOR_DESCRIPTION[1]}")
        description = self.find_element(TestSearchLocators.LOCATOR_DESCRIPTION)
        description.clear()
        description.send_keys(word)

    def content(self, word):
        logging.info(f"Send '{word}' to element {TestSearchLocators.LOCATOR_CONTENT[1]}")
        content = self.find_element(TestSearchLocators.LOCATOR_CONTENT)
        content.clear()
        content.send_keys(word)

    def click_save_btn(self):
        time.sleep(1)
        logging.info('Click button "Save"')
        self.find_element(TestSearchLocators.LOCATOR_SAVE_BTN).click()

    # ______________filling the form Contacts us________________________________________________
    def click_contact_btn(self):
        logging.info("Click contacts button")
        self.find_element(TestSearchLocators.LOCATOR_CONTACT_BTN).click()

    def name(self, word):
        logging.info(f"Send '{word}' to element {TestSearchLocators.LOCATOR_NAME_FIELD[1]}")
        name_field = self.find_element(TestSearchLocators.LOCATOR_NAME_FIELD)
        name_field.clear()
        name_field.send_keys(word)

    def email(self, word):
        logging.info(f"Send '{word}' to element {TestSearchLocators.LOCATOR_EMAIL_FIELD[1]}")
        email_field = self.find_element(TestSearchLocators.LOCATOR_EMAIL_FIELD)
        email_field.clear()
        email_field.send_keys(word)

    def content_field(self, word):
        logging.info(f"Send '{word}' to element {TestSearchLocators.LOCATOR_CONTENT_FIELD[1]}")
        content_field = self.find_element(TestSearchLocators.LOCATOR_CONTENT_FIELD)
        content_field.clear()
        content_field.send_keys(word)
        time.sleep(1)

    def click_contact_us_btn(self):
        logging.info("Click contacts button")
        self.find_element(TestSearchLocators.LOCATOR_CONTACT_US_BTN).click()


    def get_alert_message(self):
        logging.info('get text from alert')
        time.sleep(1)
        alert = self.driver.switch_to.alert
        result = alert.text
        return result

