from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.set_page_load_timeout(10)
driver.implicitly_wait(10)
driver.get("http://devmain.1tab.com/")

add = {'domain':'1tab.com', 'name':'Anuvrat', 'value':'testing'}
driver.add_cookie(add)

web_Cookies = driver.get_cookies()

for cookie in web_Cookies:
    print(cookie)
driver.close()