from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

date_to_play = '07/31/2022'
# setup the driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# open the website
driver.get("https://www.laparks.org/discover-activities?reserve=true&location=VNSO%20Pay%20Tennis")
# date selector is in iframe, so switch to it
driver.switch_to.frame('iframetpl')
# get the date selector thing
date_input_selector = driver.find_element(By.ID, 'date')
# set the date to the date we want to play
driver.execute_script("arguments[0].setAttribute('value', arguments[1])", date_input_selector, date_to_play)
# find the search button and hit enter
driver.find_element(By.ID, 'frwebsearch_buttonsearch').click()
# IMPORTANT: use the xpath of the 8am court 4 when available
driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div/form/div/div[2]/div/div/font/font/font/div/font/table/tbody/tr[2]/td/a[2]').click()
# click the add to cart button
time.sleep(2)
driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/div/button[2]').click()

time.sleep(3)