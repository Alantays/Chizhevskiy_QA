from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import math
# import time
link = "http://suninjuly.github.io/explicit_wait2.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.maximize_window()
    WebDriverWait(browser, 12).until(
            ec.text_to_be_present_in_element((By.ID, "price"), "$100")
         )
    browser.find_element(By.ID, "book").click()

    x = browser.find_element(By.ID, "input_value").text


    def c(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    y = c(x)
    browser.find_element(By.ID, "answer").send_keys(y)
    browser.find_element(By.ID, "solve").click()
    print(browser.switch_to.alert.text)
finally:
    # time.sleep(30)
    browser.quit()



