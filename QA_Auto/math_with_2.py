import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
bro = webdriver.Chrome()
link = "https://suninjuly.github.io/selects1.html"
bro.get(link)
x = bro.find_element(By.ID, "num1").text
y = bro.find_element(By.ID, "num2").text
x1 = int(x)
y1 = int(y)
c = x1 + y1
c1 = str(c)
# select = Select(bro.find_element(By.ID, "dropdown"))
# select.select_by_value(c1)
Select(bro.find_element(By.ID, "dropdown")).select_by_value(c1)
bro.find_element(By.CSS_SELECTOR, "button.btn").click()
time.sleep(10)
bro.quit()
