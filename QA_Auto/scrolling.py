from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

bro = webdriver.Chrome()
link = "http://suninjuly.github.io/execute_script.html"
bro.get(link)
x = bro.find_element(By.ID, "input_value").text
bro.execute_script("window.scrollBy(0, 100);")

def c(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

bro.find_element(By.ID, "answer").send_keys(c(x))
bro.find_element(By.ID, "robotCheckbox").click()
bro.find_element(By.ID, "robotsRule").click()
bro.find_element(By.CSS_SELECTOR, "button.btn").click()
time.sleep(10)