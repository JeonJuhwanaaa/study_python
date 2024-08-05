from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
import time
import os
from dotenv import load_dotenv

load_dotenv()


driver_option = webdriver.ChromeOptions()
driver_option.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=driver_option)

driver.get("https://tinder.com")

time.sleep(2)

login = driver.find_element(By.XPATH, value='//*[@id="o131391810"]/div/div[1]/div/main/div[1]/div/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]/div')
login.click()

time.sleep(2)
facebook_login = driver.find_element(By.XPATH, value='//*[@id="o-1596989266"]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button/div[2]/div[2]/div[2]/div/div')
facebook_login.click()

time.sleep(2)
# 틴더 창
base_window = driver.window_handles[0]

# 페북 로그인 창
fb_login_window = driver.window_handles[1]

# 포커스를 페이스북 로그인 창으로 전환하기.
driver.switch_to.window(fb_login_window)

time.sleep(2)
facebook_email = driver.find_element(By.ID, value="email")
facebook_email.send_keys(os.environ.get("FACE_BOOK_EMAIL"))

facebook_pass = driver.find_element(By.ID, value='pass')
facebook_pass.send_keys(os.environ.get("FACE_BOOK_PASS"))

facebook_pass.send_keys(Keys.ENTER)

time.sleep(3)

# 다시 틴더 페이지로 포커스 전환.
driver.switch_to.window(base_window)

time.sleep(5)
allow_location_button = driver.find_element(By.XPATH, value='//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
allow_location_button.click()

notifications_button = driver.find_element(By.XPATH, value='//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
notifications_button.click()

cookies = driver.find_element(By.XPATH, value='//*[@id="content"]/div/div[2]/div/div/div[1]/button')
cookies.click()

#Tinder free tier only allows 100 "Likes" per day. If you have a premium account, feel free to change to a while loop.
for n in range(100):
    #Add a 1 second delay between likes.
    time.sleep(1)
    try:
        print("called")
        like_button = driver.find_element(By.XPATH, value='//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_button.click()
    #Catches the cases where there is a "Matched" pop-up in front of the "Like" button:
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR, value=".itsAMatch a")
            match_popup.click()
        #Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
        except NoSuchElementException:
            time.sleep(2)