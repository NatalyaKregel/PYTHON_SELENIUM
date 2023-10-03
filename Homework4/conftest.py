import pytest, yaml
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)
    browser = testdata["browser"]


@pytest.fixture(scope="session")
def browser():
    if browser == "firefox":
        service = Service(executable_path=GeckoDriverManager().install())
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=service, options=options)
    else:
        service = Service(executable_path=ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()


S = requests.Session()


@pytest.fixture()
def create_post_restapi():
    return 'Create post RESTAPI'


@pytest.fixture()
def post_data():
    return {
        'title': 'Test for homework 4',
        'description': 'Test for homework 4',
        'content': 'Homework 4 by Kregel Natalya'
    }


@pytest.fixture()
def post_descriptions():
    return 'Test for homework 4'

