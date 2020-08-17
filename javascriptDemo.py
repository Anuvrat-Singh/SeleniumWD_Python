from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome()
baseURL = "https://app.hubspot.com/"
driver.get(baseURL)
driver.maximize_window()
driver.set_page_load_timeout(10)

wait = WebDriverWait(driver, 10)
wait.until(ec.presence_of_element_located((By.ID,"username")))

email = driver.find_element_by_id("username")
password = driver.find_element_by_id("password")
loginBtn = driver.find_element_by_id("loginBtn")
driver.execute_script("arguments[0].value='anuvrat@anuvrat.com'", email)
time.sleep(2)
#driver.execute_script("arguments[0].click", password)
driver.execute_script("arguments[0].value='incorrectPassword'", password)
time.sleep(2)
driver.execute_script("arguments[0].click", loginBtn)
#driver.execute_script("arguments[0].value='incorrectPassword'", loginBtn)
time.sleep(2)
driver.execute_script("history.go(0)")

print(driver.execute_script("return document.title"))
form = driver.find_element_by_id("hs-login")
driver.execute_script("arguments[0].style.border = '3px solid red'", form)
time.sleep(2)
driver.get("http://www.amazon.in")
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
# driver.refresh()
time.sleep(10)
stopMarker = driver.find_element(By.XPATH, "//span[text()='Up to 40% off | Household needs']")
driver.execute_script("arguments[0].scrollIntoView(true)", stopMarker)
print(driver.execute_script("return navigator.userAgent"))
time.sleep(3)
driver.close()
