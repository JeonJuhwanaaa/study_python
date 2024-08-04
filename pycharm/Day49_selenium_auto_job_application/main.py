from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
from dotenv import load_dotenv
import time

load_dotenv()

driver_option = webdriver.ChromeOptions()
driver_option.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=driver_option)

driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")

time.sleep(5)

login = driver.find_element(By.XPATH, value="/html/body/div[1]/header/nav/div/a[2]")
login.click()

time.sleep(3)

username = driver.find_element(By.ID, value="username")
username.send_keys(os.environ.get("MY_EMAIL"))
password = driver.find_element(By.ID, value="password")
password.send_keys(os.environ.get("MY_PASSWORD"))

password.send_keys(Keys.ENTER)




# driver.quit()