from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep


class TestSearchBarClass(object):
    def testSearchBar(self):
        driver = webdriver.Chrome()
        wait = WebDriverWait(driver, 5)

        # Initialize driver and open browser
        driver.get("https://www.google.com/")
        driver.maximize_window()
        wait.until(EC.presence_of_all_elements_located((By.XPATH, ".//*[@id='tsf']/div[2]/div/div[1]/div/div[1]/input")))
        sleep(3)
        driver.close()
