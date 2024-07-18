import requests
from datetime import datetime

MY_LAT = 35.167757
MY_LONG = 129.085502

# formatted -> 기본적으로 시간을 12시간 시계 형식으로 되어있음. 0 : off / 1(defalut) : on
parameterss = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

# 참고 사이트 : https://sunrise-sunset.org/api

# 해당 API 는 필수 parameter 2개(lat(위도)/lng(경도))를 갖는다. 나머진 선택사항
# 필수 파라미터를 넣지않으면 400 에러가 뜬다.
response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameterss)
response.raise_for_status()
data = response.json()
# print(data)
# T 를 중심으로 나누고 나눈것에 인덱스번호 확인 후 ":" 으로 나누기
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
# 기본적으로 12시간 시계 형식
print(sunset)
print(sunrise)
# 기본적으로 24시간 시계 형식
time_now = datetime.now()
print(time_now.hour)
