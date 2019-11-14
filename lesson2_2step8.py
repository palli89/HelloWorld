from selenium import webdriver
import time
import os
link='http://suninjuly.github.io/file_input.html'

try:
    browser=webdriver.Chrome()
    browser.get(link)
    browser.find_element_by_name("firstname").send_keys('test')
    browser.find_element_by_name("lastname").send_keys('test1')
    browser.find_element_by_name("email").send_keys('test@test.tu')
    browser.find_element_by_css_selector("#file").send_keys(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'lesson2_2step8.txt'))
    browser.find_element_by_css_selector(".btn.btn-primary").click()

finally:
    time.sleep(8)
    browser.quit()