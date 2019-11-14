from selenium import webdriver
import time
import math
link='http://suninjuly.github.io/get_attribute.html'

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser=webdriver.Chrome()
    browser.get(link)
    x=browser.find_element_by_css_selector("#treasure").get_attribute("valuex")
    browser.find_element_by_css_selector("#answer").send_keys(calc(x))
    browser.find_element_by_css_selector("#robotCheckbox").click()
    browser.find_element_by_css_selector("#robotsRule").click()
    browser.find_element_by_css_selector(".btn.btn-default").click()
finally:
    time.sleep(5)
    browser.quit()