from selenium import webdriver
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


def selectOptions(optionsList, choiceList):
    if choiceList[0] != 'all':
        for ele in optionsList:
            print(ele.text)
            for j in range(len(choiceList)):
                if ele.text == choiceList[j]:
                    ele.click()
                    break

    else:
        try:
            for ele in optionsList:
                ele.click()
        except ElementNotInteractableException:
            print("All values selected")

baseURL = "https://www.jqueryscript.net/demo/Drop-Down-Combo-Tree/"
driver = webdriver.Chrome()
driver.get(baseURL)
driver.maximize_window()
driver.set_page_load_timeout(10)
driver.implicitly_wait(10)

time.sleep(3)

driver.find_element(By.ID,'justAnInputBox').click()

time.sleep(3)

optionsList = driver.find_elements(By.XPATH, '//span[@class = "comboTreeItemTitle"]')
choiceList = ['choice 2 1', 'choice 6', 'choice 6 2 3']
#choiceList = ['all']
selectOptions(optionsList, choiceList)
