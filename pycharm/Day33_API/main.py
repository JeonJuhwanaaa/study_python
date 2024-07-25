## API -> Application Programming Interface
# a set of commands, functions, protocols, and
# objects that programmers can use to create software or interact with an external system.

import requests

# ISS Current Location API
# requests.get() 은 우리가 엔드포인트로부터 우리가 원하는 데이터를 얻도록 도와줌.
response = requests.get(url="http://api.open-notify.org/iss-now.json")
# print(response.status_code)
# if response.status_code == 404:
#     raise Exception("That resource does not exist.")
# elif response.status_code == 401:
#     raise Exception("You are not authorised to access this data.")

response.raise_for_status()
data = response.json()
# print(data)
longitude = data["iss_position"]["longitude"] # 경도
latitude = data["iss_position"]["latitude"] # 위도

iss_position = (longitude, latitude)
print(iss_position)

# << Response Codes means >>
# 1XX : Hold on
# 2XX : Here you go
# 3XX : Go away
# 4XX : You screwed up
# 5XX : I screwed up