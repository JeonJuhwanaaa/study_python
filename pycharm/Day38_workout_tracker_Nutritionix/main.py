import requests
from _datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

EXERCISE_TEXT = input("Tell me which exercise you did: ")
GENDER = "male"
WEIGHT_KG = "70"
HEIGHT_CM = "175"
AGE = "30"

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/79ebe14e40c5b3ee66f3e29978b8339a/juhwanWorkouts/workouts"

headers = {
    "x-app-id": os.environ.get("NUTRITIONIX_APP_ID"),
    "x-app-key": os.environ.get("NUTRITIONIX_API_KEY"),
    "Content-Type": "application/json"
}

# print(os.environ.get("NUTRITIONIX_API_ID"))

params = {
    "query": EXERCISE_TEXT,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=nutritionix_endpoint, headers=headers, json=params)
response.raise_for_status()
# print(response.json())
result = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(url=sheet_endpoint, json=sheet_inputs)
    print(sheet_response.text)