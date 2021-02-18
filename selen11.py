import os
import time
import pyperclip
from selenium import webdriver
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element_by_class_name("btn.btn-primary").click()
    confirm = browser.switch_to.alert
    confirm.accept()
    x_element = browser.find_element_by_id("input_value")
    x = int(x_element.text)
    answer = calc(x)
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(answer)
    browser.find_element_by_class_name("btn.btn-primary").click()
    alert = browser.switch_to.alert
    alert_text = alert.text
    addToClipBoard = alert_text.split(': ')[-1]
    pyperclip.copy(addToClipBoard)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
