from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome()

driver.get('https://swisnl.github.io/jQuery-contextMenu/demo.html')
driver.maximize_window()
driver.set_page_load_timeout(10)
driver.implicitly_wait(10)

mouseEle = driver.find_element(By.XPATH, "//span[@class='context-menu-one btn btn-neutral']")
actChain = ActionChains(driver)
actChain.context_click(mouseEle).perform()
rightClick_Options = driver.find_elements(By.XPATH, "//li[contains(@class,'context-menu-icon')]")

for ele in rightClick_Options:
    if ele.text == 'Copy':
        ele.click()
        break;