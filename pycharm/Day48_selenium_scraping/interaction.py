from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


## Challenge
# Create a blank file called interaction.py. Use Selenium to print the total
# number of articles from the Wikipedia homepage to the PyCharm console.

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_option)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

# article_num = driver.find_element(By.ID,value="articlecount")
# print(article_num.text.split(" ")[0])
article_num = driver.find_element(By.CSS_SELECTOR,value="#articlecount a")
# print(article_num.text)

# 버튼 누르기.
# article_num.click()

# a 태그 클릭
all_portals = driver.find_element(By.LINK_TEXT, value="View source")
# all_portals.click()

## ----------------------------------------------------------------------------------
# 돋보기 버튼 클릭 -> 입력 -> enter 로 들어가기.
search_button = driver.find_element(By.CSS_SELECTOR, value=".vector-header-end a")
search_button.click()
# 입력 창에 입력
search = driver.find_element(By.NAME, value="search")
search.send_keys("Python")
# 검색창에 입력하고 ENTER 키 눌러준다.
search.send_keys(Keys.ENTER)


# driver.quit()