from selenium import webdriver
import time
import math
link='http://suninjuly.github.io/redirect_accept.html'

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser=webdriver.Chrome()
    browser.get(link)
    browser.find_element_by_css_selector(".trollface.btn.btn-primary").click()
    browser.switch_to.window(browser.window_handles[1])
    x = browser.find_element_by_css_selector("#input_value").text
    browser.find_element_by_css_selector("#answer").send_keys(calc(x))
    browser.find_element_by_css_selector(".btn.btn-primary").click()

finally:
    time.sleep(8)
    browser.quit()