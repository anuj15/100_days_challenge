import math
from datetime import datetime as dt

import requests

from api_requests.others.data import *

nutrition_headers = {
    "x-app-id": NUTRITION_APP_ID,
    "x-app-key": NUTRITION_API_KEY,
    "Content-Type": CONTENT_TYPE,
}

nutrition_parameters = {
    "query": "ran 2 miles and walked for 3Km",
    "gender": "male",
    "weight_kg": 80,
    "height_cm": 160,
    "age": 32,
}

nutrition_response = requests.post(url=NUTRITION_ENDPOINT, headers=nutrition_headers, json=nutrition_parameters)
nutrition_exercise = nutrition_response.json()["exercises"]
data = [[math.floor(x["duration_min"]), math.floor(x["nf_calories"]), x["name"].title(), dt.now().strftime("%d/%m/%Y"),
         dt.now().strftime("%H:%M:%S")] for x in nutrition_exercise]

for row in data:
    header = {
        "Content-Type": CONTENT_TYPE,
        "Authorization": SHEETY_BASIC_AUTH,
    }
    sheety_parameters = {
        "workout": {
            "duration": row[0],
            "calories": row[1],
            "exercise": row[2],
            "date": row[3],
            "time": row[4],
        }
    }
    sheety_response = requests.post(url=SHEETY_ENDPOINT, json=sheety_parameters, headers=header)
    sheety_response.raise_for_status()
    print(sheety_response.json())

if __name__ == '__main__':
    print("")
