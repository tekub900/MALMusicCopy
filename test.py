import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

os.environ['PATH'] += r"C:/SeleniumDrivers"
driver = webdriver.Chrome()
driver.get("https://myanimelist.net/topanime.php")
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@id='qc-cmp2-ui']/div[2]/div/button[3]"))
    )
    popup = driver.find_element(By.XPATH, "//div[@id='qc-cmp2-ui']/div[2]/div/button[3]")
#    print(element.text)
    popup.click()
    link = driver.find_element(By.ID, '#area43608')
    link.click()
    table = driver.find_element(By.XPATH, "//div[@class='theme-songs js-theme-songs opnening']/table")
#    print(table.text)
    rows = table.find_elements(By.TAG_NAME, 'tr')
    for row in rows:
        col = row.find_elements(By.TAG_NAME, 'td')[1]
        print(col.text)
#    driver.get("https://www.youtube.com/")
#    theme_song_title = driver.find_element(By.CLASS_NAME, 'theme-song-title')
#    theme_song_artist = driver.find_element(By.CLASS_NAME, 'theme-song-artist')
#    print(theme_song_artist.text)
#    print(theme_song_title.text)
except TimeoutException:
    print("Timeout alert!")
finally:
    driver.quit()
# my_element = driver.find_element("#area5114")
# my_element.click()
