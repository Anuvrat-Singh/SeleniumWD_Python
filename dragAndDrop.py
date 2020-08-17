from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome()
driver.get('https://jqueryui.com/resources/demos/droppable/default.html')
driver.maximize_window()
driver.set_page_load_timeout(10)
driver.implicitly_wait(10)

source = driver.find_element(By.ID,'draggable')
target = driver.find_element(By.ID, 'droppable')
#time.sleep(5)

actChain = ActionChains(driver)
#actChain.drag_and_drop(source,target).perform()
actChain.click_and_hold(source).move_to_element(target).release().perform()
time.sleep(5)

driver.quit()