# scraping 라이브러리
import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv
import lxml

# 이메일 전송 라이브러리
import smtplib

load_dotenv()
url = "https://www.amazon.com/SLICE-RED-Android13-Smartphone-Fingerprint/dp/B0D5BN258W/ref=sr_1_9?crid=1D68JQ3R0E9G1&dib=eyJ2IjoiMSJ9.wLVCibRh4NX3wxMrXb_CgWEANsSVnxOC2FD_nw48Z0uy91gIZr_gVPgX_xmW3z990VQrXbgjg8omvWAXBmd8fsYvYLWw-df31Ji0WFK9DwF3SiXGl8mPrn7neT-62t5t0KOhJdEPzw8k5KgU6O4ndE1a8vnz6vaCH4dz8hq5wUfZhqZRVeVyVJIlRscfA4FA.cwZAWIpQ8TgPhVjMU6kS3r4oSrtyailTJfmL4iu-5kE&dib_tag=se&keywords=iphone&psr=EY17&qid=1722490843&s=todays-deals&sprefix=iphone%2Ctodays-deals%2C260&sr=1-9-catcorr&th=1"

response = requests.get(
    url=url,
    headers={
        "User-Agent":os.environ.get("USER_AGENT"),
        "Accept-Language":os.environ.get("ACCEPT_LANGUAGE")
    }
    )
product = response.text
# print(product)
soup = BeautifulSoup(product, "lxml")
# print(soup.find("span", class_="a-offscreen").get_text())
price = soup.find("span", class_="a-offscreen").get_text()
price_without_currency = price.split("$")[1] # $ 기준으로 두개로 나눈 후 후자꺼를 가져오는 거니깐 인덱스 번호 1 로 함.
price_as_float = float(price_without_currency)
print(price_without_currency)

# 이메일 전송
# 내가 원하는 가격이 되면 이메일로 알려주기.
title = soup.find(id="productTitle").get_text().strip()
print(title)

BUY_PRICE = 200
MY_GMAIL_EMAIL = os.environ.get("MY_GMAIL_EMAIL")
MY_GMAIL_PASSWORD = os.environ.get("MY_GMAIL_SEC_PASSWORD")
MY_NAVER_EMAIL = os.environ.get("MY_NAVER_EMAIL")

if price_as_float < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login(MY_GMAIL_EMAIL, MY_GMAIL_PASSWORD)
        connection.sendmail(
            from_addr=MY_GMAIL_EMAIL,
            to_addrs=MY_NAVER_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")
        )