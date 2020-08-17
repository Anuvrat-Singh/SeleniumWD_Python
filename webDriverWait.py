from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome()
baseURL = "https://app.hubspot.com/"
driver.get(baseURL)
driver.maximize_window()
driver.set_page_load_timeout(10)
# driver.implicitly_wait(10)

wait = WebDriverWait(driver, 15)
#webElement = wait.until(ec.visibility_of_element_located((By.ID, "username")))
#webElement.send_keys("Hakuna Matata")
print(driver.title)
wait.until(ec.title_contains('HubSpot'))
print(driver.title)
#time.sleep(3)
driver.close()

