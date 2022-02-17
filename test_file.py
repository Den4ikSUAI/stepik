import math
import os
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time 


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element_by_id('button').click()
    browser.switch_to.window(browser.window_handles[1])
    x_string = browser.find_element_by_id("input_value")
    x_number = int(x_string.text)

    # высчитываем результат для задания
    answer = calc(x_number)
    input_answer = browser.find_element_by_id("answer")
    input_answer.send_keys(answer)
    send_button = browser.find_element_by_class_name("btn-primary")
    send_button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла