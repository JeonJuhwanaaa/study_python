import requests
from dotenv import load_dotenv
from twilio.rest import Client
import os

load_dotenv()

# https://openweathermap.org/  -> 날씨 open API 사이트
## 버전 3.0 에선 401 코드로 오류.
## 버전을 3.0 에서 2.8 로 수정하니 200 코드로 정상.
OWN_Endpoint = "https://api.openweathermap.org/data/2.8/onecall"

api_key = ""
account_sid = ""
auth_token = ""

weather_params = {
    "lat": 35.174606,
    "lon": 129.066784,
    "appid": api_key,
    "exclude": "current,minutely,daily" # option
}

response = requests.get(OWN_Endpoint, params=weather_params)
# print(response.status_code)
response.raise_for_status()
# print(response.json())
weather_data = response.json()

# << Challenge >>
# < Objective > print "Bring an Umbrella" if any of the next 12 hourly weather condition codes is less than 700.
# Hint:
# 1) Practice printing out the weather ID for the weather in the 0th hour.
# 2) Try to create a slice from the weather data to get a list of the hourly forecasts for only the next 12 hours.
# 3) Using the above try to create a list of only the next 12 weather condition codes.

# print(weather_data["hourly"][1]["weather"][0]["id"])
# print(len(weather_data["hourly"]))

## 스스로 한 것.

# for n in range(len(weather_data["hourly"])):
#     print(weather_data["hourly"][n]["weather"][0]["id"])
#     if weather_data["hourly"][n]["weather"][0]["id"] < 700:
#         print("Bring an Umbrella")

# ------------------------------------------------------
# 강의에서 한 것.

weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        # print("Bring an Umbrella.")
        will_rain = True
if will_rain:
    # print("Bring an Umbrella.")
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="",
        from_="",
        to=""
    )
    print(message.status)
