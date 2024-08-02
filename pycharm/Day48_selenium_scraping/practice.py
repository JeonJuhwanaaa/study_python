from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Challenge
# Practice using Selenium fill in this form and clicking Sign Up
# (this is not a real registration page)


driver_option = webdriver.ChromeOptions()
driver_option.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=driver_option)
driver.get("https://secure-retreat-92358.herokuapp.com/")


first_name = driver.find_element(By.NAME, value="fName")
first_name.send_keys("Jeon")

last_name = driver.find_element(By.NAME, value="lName")
last_name.send_keys("juhwan")

email = driver.find_element(By.NAME, value="email")
email.send_keys("1q2w3e4r@naver.com")

# sign_up_button = driver.find_element(By.CLASS_NAME, value="btn btn-lg btn-primary btn-block")
# sign_up_button.click()

email.send_keys(Keys.ENTER)


# driver.quit()