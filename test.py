import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

os.environ['PATH'] += r"C:/SeleniumDrivers"
driver = webdriver.Edge()
driver.get("https://myanimelist.net/topanime.php")
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@id='qc-cmp2-ui']/div[2]/div/button[3]"))
    )
    alert = driver.find_element(By.XPATH, "//div[@id='qc-cmp2-ui']/div[2]/div/button[3]")
#    print(element.text)
    alert.click()
#    print("alert accepted")
except TimeoutException:
    print("no alert")
# finally:
#    driver.quit()
# my_element = driver.find_element("#area5114")
# my_element.click()
