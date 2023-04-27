import requests
import urllib3
from twilio.rest import Client

from api_requests.others.data import *

urllib3.disable_warnings()

END_POINT = "https://api.openweathermap.org/data/2.5/onecall"
PARAMETERS = {
    "lat": 45.527901,
    "lon": -79.317093,
    "appid": OWM_API_KEY,
    "exclude": "current,minutely,daily"
}
response = requests.get(url=END_POINT, params=PARAMETERS)
response.raise_for_status()
response_json = response.json()
response_hourly = response_json["hourly"]
response_slice = response_hourly[:12]
ids = [x["weather"][0]["id"] for x in response_slice if x["weather"][0]["id"] > 700]
if len(ids) > 0:
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        body="Its going to rain today. Remember to bring an Umbrella!",
        from_=TWILIO_FROM_PHONE_NUMBER,
        to=MY_PHONE_NUMBER,
        force_delivery=True
    )
    print(message.status)

if __name__ == '__main__':
    print("")
