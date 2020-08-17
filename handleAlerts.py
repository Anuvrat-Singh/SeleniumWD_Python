from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.set_page_load_timeout(10)
driver.implicitly_wait(10)
# driver.get("https://www.seleniumeasy.com/test/javascript-alert-box-demo.html")
#
# button = driver.find_element(By.XPATH, "(//button[text()='Click me!'])[1]")
# button.click()
# alert = driver.switch_to.alert
# alert.accept()
# driver.switch_to.default_content()
# driver.refresh()
# button = driver.find_element(By.XPATH, "(//button[text()='Click me!'])[1]")
# button.click()
# alert = driver.switch_to.alert
# alert.dismiss()
# driver.switch_to.default_content()
# time.sleep(3)
# driver.refresh()
# confirm = driver.find_element(By.XPATH, "(//button[text()='Click me!'])[2]")
# confirm.click()
# alert = driver.switch_to.alert
# alert.accept()
# driver.switch_to.default_content()
# driver.refresh()
# confirm = driver.find_element(By.XPATH, "(//button[text()='Click me!'])[2]")
# confirm.click()
# alert = driver.switch_to.alert
# alert.dismiss()
# driver.switch_to.default_content()
# driver.refresh()
# message = driver.find_element(By.XPATH, "(//button[text()='Click for Prompt Box'])")
# message.click()
# alert = driver.switch_to.alert
# alert.send_keys("Anuvrat")
# alert.accept()
# driver.switch_to.default_content()
# driver.refresh()
# message = driver.find_element(By.XPATH, "(//button[text()='Click for Prompt Box'])")
# message.click()
# alert = driver.switch_to.alert
# alert.dismiss()
# driver.switch_to.default_content()

driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
time.sleep(3)
driver.close()
