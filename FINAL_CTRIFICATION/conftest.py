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


@pytest.fixture()
def finding_about():				#отображение кнопки about
    return 'About Page'


@pytest.fixture()
def click_about():					#нажатие кнопки about
    return 'Click button about'


@pytest.fixture()
def about_font():		            #размер шрифта заголовка about
    return '32px'


@pytest.fixture()
def expected_username():            #ожидаемое имя пользователя
    return "web1"

@pytest.fixture()
def get_nikto_command():
    return "nikto -h https://test-stand.gb.ru/ -ssl -Tuning 4"      #проверка на уязвимость сайта с исп.утилиты nikto


@pytest.fixture()
def expected_result() -> str:       # ожидаемый результат после команды
    return '0 error(s)'

