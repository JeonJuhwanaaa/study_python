from bs4 import BeautifulSoup
import lxml
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
articles = soup.find_all("a")
print(articles)

article_texts = []
article_links = []

for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
# print(article_upvotes)

largest_number = max(article_upvotes)
print(largest_number)
largest_index = article_upvotes.index(largest_number)
print(largest_index)

print(article_texts[largest_index])
print(article_links[largest_index])


# ------------------------------------------------------------------------------------------------------------------

# # BeautifulSoup 공식문서 -> https://www.crummy.com/software/BeautifulSoup/bs4/doc/
#
# # 파일 불러오기.
# # 웹 스크래핑 / 파싱 -> 웹 페이지의 html을 분석하고 필요한 정보를 추출.
#
# # UnicodeDecodeError: 'cp949' codec can't decode byte 0xe2 in position 280: illegal multibyte sequence
# # 위와 같은 에러가 발생한 경우,
# # encoding="UTF8" 추가해주면 된다.
# # 해당 에러는 파일 인코딩 불일치, 즉 파일이 실제로 다른 인코딩(CP949가 아닌 UTF-8, ISO-8859-1 등)으로
# # 인코딩되었는데, 잘못된 인코딩(CP949)으로 읽으려고 할 때 발생한다.
# with open("website.html", encoding="UTF8") as file:
#     contents = file.read()
#
# # BeautifulSoup 의 매개변수에 있는 html.parser 대신 lxml 가능
# # 특정 웹 사이트의 경우 html.parser 가 작동하지 않는 경우가 있으며
# # 그럴 경우 lxml 사용하면 된다.
# soup = BeautifulSoup(contents,"html.parser")
#
# # print(soup.title.string)
# # print(soup.title)
# # print(soup.prettify())
# # print(soup.p)
#
# # ------------------------------------------------------------
#
# # 하나의 태그를 찾는 것 보다 모든 p 태그나 모든 앵커 등 모든 태그 찾기.
# all_anchor_tags = soup.find_all(name="a")
# # print(all_anchor_tags)
#
# # for tag in all_anchor_tags:
#     # 앵커 태그에서 텍스트만 가져오기. -> for문 사용
#     # print(tag.getText())
#     # --------------------------------------------------------
#     # 하이퍼텍스트만 가져오기.
#     # tag_href = tag.get("href")
#     # print(tag_href)
#
# # 많은 h1 태그 중 id 로 특정 h1 태그 찾기.
# heading = soup.find(name="h1", id="name")
# # print(heading)
#
# # 매개변수로 class 키워드는 파이썬의 예약 키워드이기 때문에 클래스를 생성하는 데만 사용되는 특수단어이다.
# # 대신 class_ 를 사용해준다.
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.get("class"))
#
# name = soup.select_one(selector="#name")
# print(name)
#
# headings = soup.select(".heading")
# print(headings)