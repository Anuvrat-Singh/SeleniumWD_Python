from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
baseURL = "https://opensource-demo.orangehrmlive.com/"
driver.get(baseURL)
driver.maximize_window()
driver.set_page_load_timeout(10)
driver.implicitly_wait(10)

driver.find_element(By.XPATH,"//input[@id='txtUsername']").send_keys("Admin")
driver.find_element(By.ID,"txtPassword").send_keys("admin123")
driver.find_element(By.NAME,"Submit").click()

print("Title is: " + driver.title)

driver.find_element(By.LINK_TEXT, 'Admin').click()

userRole_Dropdown = driver.find_element(By.ID, 'searchSystemUser_userType')
userRole_Options = Select(userRole_Dropdown)

#select admin from the options

userRole_Options.select_by_visible_text('Admin')
print("Admin is selected")
userRole_Options.select_by_index(2)
print("ESS is selected")
userRole_Options.select_by_value("0")
print("All is selected now")

print(userRole_Options.is_multiple)

