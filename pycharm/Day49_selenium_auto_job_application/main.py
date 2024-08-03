from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver_option = webdriver.ChromeOptions()
driver_option.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=driver_option)

driver.get("https://www.linkedin.com/home")
login = driver.find_element(By.CLASS_NAME, value=".nav__button-secondary btn-md btn-secondary-emphasis")
login.click()




# driver.quit()