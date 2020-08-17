from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()
driver.set_page_load_timeout(10)
driver.implicitly_wait(10)

driver.get_screenshot_as_file('spicejet.png')
driver.close()