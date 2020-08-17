from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome()
driver.get('https://codepen.io/rcass/pen/MmYwEp')
driver.maximize_window()
driver.set_page_load_timeout(10)
driver.implicitly_wait(10)
driver.switch_to.frame("result")
driver.find_element(By.ID, 'fileToUpload').send_keys('/home/deadpool/Desktop/img2_cccqio.png')
time.sleep(2)
driver.find_element(By.NAME, 'submit').click()
time.sleep(2)
driver.close()