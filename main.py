import requests
from datetime import date
import  datetime as dt

# ------------------------------ PROFILE ------------------------------ #

GENDER = "male"
WEIGHT = 86.1
HEIGHT = 180.34
AGE = 28


headers = {
    "x-app-id" : "462425a2",
    "x-app-key" : "5372c30359c4eb09d6b0d5ff55cd1c58"
}

workout_data = {
 "query":"",
 "gender": GENDER,
 "weight_kg": WEIGHT,
 "height_cm": HEIGHT,
 "age": AGE
}

workout_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"


g_sheet_endpoint = "https://api.sheety.co/7841abbd283b105c897f80243e2cbdf2/myWorkouts/workouts"

# g_reponse = requests.post(url=g_sheet_endpoint,json=g_data)

user_response = input("What workout did you do today? ")

workout_data["query"] =  user_response

workout_response = requests.post(url=workout_endpoint,json=workout_data,headers=headers)

excercises = workout_response.json()['exercises']

for workout in excercises:

    g_data = {
        "workout": {
            "date": str(date.today()),
            "time": str(dt.datetime.now()),
            "exercise": workout['user_input'],
            "duration": workout["duration_min"],
            "calories": workout["nf_calories"]
        }
    }

    g_reponse = requests.post(url=g_sheet_endpoint,json=g_data)

