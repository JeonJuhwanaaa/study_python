import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import InternetSpeedTwitterBot


load_dotenv()

PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_EMAIL = os.environ.get("TWITTER_EMAIL")
TWITTER_PASS = os.environ.get("TWITTER_PASSWORD")
