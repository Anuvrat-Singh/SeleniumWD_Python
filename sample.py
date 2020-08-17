from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class firefoxSample():
    def firefox_sample_test(self):
        baseURL = "https://opensource-demo.orangehrmlive.com/"
        driver = webdriver.Firefox(executable_path="/usr/local/bin/geckodriver")
        driver.get(baseURL)
        driver.maximize_window()

        driver.set_page_load_timeout(10)
        driver.implicitly_wait(10)

        driver.find_element(By.XPATH,"//input[@id='txtUsername']").send_keys("Admin")
        driver.find_element(By.ID,"txtPassword").send_keys("admin123")
        driver.find_element(By.NAME,"Submit").click()

        print("Title is: " + driver.title)

        driver.find_element(By.LINK_TEXT, 'Admin').click()

        link_text = driver.find_elements(By.TAG_NAME, 'a')

        for element in link_text:
            print(element.text)
            print(element.get_attribute('href'))




    # def chromeSample(self):
    #     driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
    #     driver.get("https://shop.demoqa.com/")


ff = firefoxSample()
ff.firefox_sample_test()
#ff.chromeSample()