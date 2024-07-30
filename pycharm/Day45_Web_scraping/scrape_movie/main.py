from bs4 import BeautifulSoup
import requests

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
# print(response.text)
movie_page = response.text

soup = BeautifulSoup(movie_page, "html.parser")
# print(soup.find_all("h3"))
all_movies = soup.find_all("h3", class_="title")
# print(all_movies)


# -----------------------------------------
# movie_titles = []
# for movie in all_movies:
#     movie_titles.append(movie.getText())
# movies = movie_titles[::-1] # 역순
# print(movies)
# -----------------------------------------
# 위 코드와 같은 뜻.
movie_titles = [movie.getText() for movie in all_movies]
movies = movie_titles[::-1] # 역순
print(movies)

with open("movies.txt", mode="w", encoding="UTF-8") as file:
    for movie in movies:
        file.write(f"{movie}\n")