from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
from dotenv import load_dotenv
import time
from selenium.common.exceptions import ElementClickInterceptedException


load_dotenv()

SIMILAR_ACCOUNT = "jjuuhwan"
USERNAME = os.environ.get("INSTA_EMAIL")
PASSWORD = os.environ.get("INSTA_PASSWORD")

class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(2)
        username = self.driver.find_element(By.NAME, value='username')
        password = self.driver.find_element(By.NAME, value='password')

        username.send_keys(USERNAME)
        password.send_keys(PASSWORD)

        password.send_keys(Keys.ENTER)
        time.sleep(5)

    def find_followers(self):
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/")
        time.sleep(5)
        followers = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers.click()

        # 스크롤 하는 법
        time.sleep(2)
        modal = self.driver.find_element(By.XPATH, value='/html/body/div[4]/div/div/div[2]')

        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        time.sleep(5)

        def follow(self):
            all_buttons = self.driver.find_elements(By.CSS_SELECTOR, value="li button")
            for button in all_buttons:
                # 이미 팔로우가 된 사람을 클릭 시 ElementClickInterceptedException 에러 발생.
                try:
                    button.click()
                    time.sleep(1)
                except ElementClickInterceptedException:
                    # 이미 팔로우된 사람의 모달이 켜지면 취소 누르기.
                    cancel_button = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
                    cancel_button.click()


bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()