from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


driver = webdriver.Chrome()
driver.get("https://www.spicejet.com/default.aspx")
driver.maximize_window()
driver.set_page_load_timeout(10)
driver.implicitly_wait(10)

loginBtn = driver.find_element(By.ID, 'ctl00_HyperLinkLogin')
actChain = ActionChains(driver)
actChain.move_to_element(loginBtn).perform()

spcMembers = driver.find_element(By.LINK_TEXT, 'SpiceClub Members')
actChain.move_to_element(spcMembers).perform()

memberLogin = driver.find_element(By.LINK_TEXT, 'Member Login')
memberLogin.click()
time.sleep(3)

driver.close()