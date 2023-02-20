import time
from selenium import webdriver
from selenium.webdriver.common.by import By
try:
    link = "http://suninjuly.github.io/file_input.html"
    bro = webdriver.Chrome()
    bro.get(link)
    bro.find_element(By.TAG_NAME, "input").send_keys("Kirill")
    bro.find_element(By.NAME, "lastname").send_keys("Chizh")
    bro.find_element(By.NAME, "email").send_keys("EMAIL")
    bro.find_element(By.ID, "file").send_keys("C:/Users/Kirill/Desktop/css.txt")
    bro.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
    time.sleep(10)
    bro.quit()
