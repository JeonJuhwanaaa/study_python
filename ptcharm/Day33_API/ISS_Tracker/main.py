import requests
from datetime import datetime
import smtplib
import time

MY_EMAIL = ""
MY_PASSWORD = ""

MY_LAT = 35.167757
MY_LONG = 129.085502

def is_iss_overheard():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"]) #위도
    iss_longitude = float(data["iss_position"]["longitude"]) #경도
    print((iss_latitude, iss_longitude))

    #Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT -5 <= iss_latitude <= MY_LAT + 5 and MY_LONG -5 <= iss_longitude <= MY_LONG + 5:
        return True

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0, # 시간을 24시간 시계 형식
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    # print(time_now)

    if time_now >= sunset or time_now <= sunrise:
        return True


# If the ISS is close to my current position
# and it is currently dark
# Then send mean email to tell me to look up.
# BONUS: run the code every 60 seconds.

while True:
    time.sleep(60)
    if is_iss_overheard() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject:Look Up\n\nthe ISS is above you in the sky."
        )