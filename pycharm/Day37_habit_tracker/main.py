import requests
from datetime import datetime

# https://pixe.la/v1/users/juhwan/graphs/graph1.html

# api 가져오기.

# 임의로 지정
USERNAME = "juhwan"
TOKEN = "abmlkgnbl324kowf2k34"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# ------------------------------------------------------------------------------------------

# header 로 authentication(인증)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# post 요청
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# ------------------------------------------------------------------------------------------

# 날짜 / km 수 데이터 입력 넣기.

pixel_create_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()
# print(today.strftime("%y%m%d"))
# today = datetime(year=2024, month=7, day=27)

pixel_data = {
    # "date": "20240728",
    "date": today.strftime("%Y%m%d"), # %Y -> 년도(Y 대문자) / %m -> 달 / %d -> 날
    "quantity": input("How many kilometers did you cycle today? ")
}

response = requests.post(url=pixel_create_endpoint, json=pixel_data, headers=headers)
print(response.text)

# ------------------------------------------------------------------------------------------

# PUT 요청

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
new_pixel_data = {
    "quantity": "4.5"
}

# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)

# ------------------------------------------------------------------------------------------

# Delete 요청

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)