from selenium import webdriver
from selenium.webdriver.common.by import By

import time

driver=webdriver.Chrome()

driver.get("https://comic.naver.com/webtoon")

time.sleep(1)

webtoonMenu = driver.find_element(by=By.XPATH, value='//*[@id="menu"]/li[2]/a')
webtoonMenu.click()

time.sleep(1)

webtoonDict = {
    "월": [],
    "화": [],
    "수": [],
    "목": [],
    "금": [],
    "토": [],
    "일": []
}

dayList = list(webtoonDict.keys())

for day in dayList:
    webtoonDayMenus = driver.find_elements(by=By.CSS_SELECTOR, value='.SubNavigationBar__link--PXX5B')
    print(webtoonDayMenus)

    for menu in webtoonDayMenus:
        if menu.text != day:
            continue

        menu.click()
        time.sleep(1)

        scrollTop = 0
        while True:
            driver.execute_script(f"window.scrollTo(0, {scrollTop})")

            scrollTop += 500
            if scrollTop > driver.execute_script("return document.body.scrollHeight"):
                break

        webtoonList = []
        webtoonItems = driver.find_elements(by=By.CSS_SELECTOR, value='.ContentList__content_list--q5KXY .item')
        for item in webtoonItems:
            title = item.find_element(by=By.CSS_SELECTOR, value='.ContentTitle__title--e3qXt .text').text
            author = item.find_element(by=By.CSS_SELECTOR, value='.ContentAuthor__author--CTAAP').text
            rating = item.find_element(by=By.CSS_SELECTOR, value='.Rating__star_area--dFzsb .text').text
            imgUrl = item.find_element(by=By.CSS_SELECTOR, value='.Poster__image--d9XTI').get_attribute(name="src")

            webtoon = {
                "title": title,
                "author": author,
                "rating": float(rating),
                "imgUrl": imgUrl
            }
            webtoonList.append(webtoon)

    webtoonDict.update({day: webtoonList})