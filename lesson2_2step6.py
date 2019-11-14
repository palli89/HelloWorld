from selenium import webdriver
import time
import math
link='http://SunInJuly.github.io/execute_script.html'

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser=webdriver.Chrome()
    browser.get(link)
    x=browser.find_element_by_css_selector("#input_value").text
    browser.find_element_by_css_selector("#answer").send_keys(calc(x))
    browser.find_element_by_css_selector("#robotCheckbox").click()
    browser.execute_script("window.scrollBy(0, 100);")
    browser.find_element_by_css_selector("#robotsRule").click()
    browser.find_element_by_css_selector(".btn.btn-primary").click()


finally:
    time.sleep(8)
    browser.quit()