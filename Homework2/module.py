'''Задание 1.
Добавить в тестовый проект шаг добавления поста после входа. Должна выполняться
проверка на наличие названия поста на странице сразу после его создания.
Совет:
Не забудьте добавить небольшие ожидания перед и после нажатия кнопки создания поста.'''


import yaml
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)
    browser = testdata["browser"]


class Site:
    def __init__(self, address):
        if browser == "firefox":
            service = Service(executable_path=GeckoDriverManager().install())
            options = webdriver.FirefoxOptions()
            self.driver = webdriver.Firefox(service=service, options=options)

        elif browser == "chrome":
            service = Service(executable_path=ChromeDriverManager().install())
            options = webdriver.ChromeOptions()
            self.driver = webdriver.Chrome(service=service, options=options)

        self.driver.implicitly_wait(testdata["sleep_time"])
        self.driver.maximize_window()
        self.driver.get(address)

    def find_element(self, mode, path):
        if mode == "css":
            element = self.driver.find_element(By.CSS_SELECTOR, path)
        elif mode == "xpath":
            element = self.driver.find_element(By.XPATH, path)
        elif mode == "id":
            element = self.driver.find_element(By.ID, path)
        else:
            element = None
        return element

    def get_element_property(self, mode, path, property):
        element = self.find_element(mode, path)
        return element.value_of_css_property(property)

    def close(self):
        self.driver_close()
