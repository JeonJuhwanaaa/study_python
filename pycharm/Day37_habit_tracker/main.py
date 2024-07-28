import requests
from datetime import datetime

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

# https://pixe.la/v1/users/juhwan/graphs/graph1.html

pixel_create_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

# today = datetime.now()
# print(today.strftime("%y%m%d"))
today = datetime(year=2024, month=7, day=27)


pixel_data = {
    # "date": "20240728",
    "date": today.strftime("%y%m%d"),
    "quantity": "15"
}

# response = requests.post(url=pixel_create_endpoint, json=pixel_data, headers=headers)
# print(response.text)

