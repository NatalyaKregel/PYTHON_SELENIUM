'''
Задание
Условие: Добавить в наш тестовый проект шаг добавления поста после входа. 
Должна выполняться проверка на наличие названия поста на странице сразу после его создания.
Совет: не забудьте добавить небольшие ожидания перед и после нажатия кнопки создания поста.
'''
import time
import yaml
from selenium.webdriver.common.by import By

from module import Site


with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)

site = Site(testdata["address"])


#авторизация пользователя
def test_step3(x_selector1, x_selector2, x_selector4, btn_selector, account_name):
    input1 = site.find_element("xpath", x_selector1)
    input1.clear()
    input1.send_keys(testdata["login"])
    input2 = site.find_element("xpath", x_selector2)
    input2.clear()
    input2.send_keys(testdata["pswd"])
    btn = site.find_element("css", btn_selector)
    btn.click()
    code_label = site.find_element("xpath", x_selector4).text
    assert code_label == account_name, "test_step3 Failed"


def test_step4_create_new_post(title_check):
    time.sleep(1)
    btn2 = site.find_element("id", testdata['btn2'])
    btn2.click()
    time.sleep(1)

    input1 = site.find_element("xpath", testdata['input1'])
    input1.send_keys(testdata["title_post"])

    input2 = site.find_element("xpath", testdata['input2'])
    input2.send_keys(testdata["description_post"])

    input3 = site.find_element("xpath", testdata['input3'])
    input3.send_keys(testdata["content_post"])

    site.find_element("xpath", testdata['btn3']).click()

    code_label = site.find_element("css", testdata['btn_save_selector']).text

    assert code_label == title_check, "test_step4 Failed"


