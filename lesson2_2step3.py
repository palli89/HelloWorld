from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select
link='http://suninjuly.github.io/selects1.html'

try:
    browser=webdriver.Chrome()
    browser.get(link)
    sum=int(browser.find_element_by_css_selector("#num1").text)+int(browser.find_element_by_css_selector("#num2").text)
    Select(browser.find_element_by_css_selector("#dropdown")).select_by_visible_text(str(sum))
    browser.find_element_by_css_selector(".btn.btn-default").click()


finally:
    time.sleep(5)
    browser.quit()