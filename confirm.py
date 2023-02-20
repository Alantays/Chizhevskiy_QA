import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
link = "http://suninjuly.github.io/alert_accept.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    browser.switch_to.alert.accept()

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    def c(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    y = c(x)
    browser.find_element(By.ID, "answer").send_keys(y)
    time.sleep(1)
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
finally:
    time.sleep(10)
    browser.quit()
