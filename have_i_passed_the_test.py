import time
from selenium import webdriver
from selenium.webdriver.common.by import By
try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/registration1.html")
    elements = browser.find_elements(By.CSS_SELECTOR, "input[required]")
    for element in elements:
        element.send_keys("111")
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    time.sleep(1)
    welcome_text = browser.find_element(By.TAG_NAME, "h1").text
    # assert "Congratulations! You have successfully registered!" == welcome_text
    if welcome_text == "Congratulations! You have successfully registered!":
        print("Test passed")
    else:
        print("Test failed")
finally:
    time.sleep(10)
    browser.quit()