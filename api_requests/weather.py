import os

import requests
import urllib3
from twilio.http.http_client import TwilioHttpClient
from twilio.rest import Client

urllib3.disable_warnings()

TWILIO_SID = "AC223ecbcc3ac60900229dd2c0628095f6"
TWILIO_AUTH_TOKEN = "c7692b4d0437db5622ce1eb995f8992d"
TWILIO_PHONE_NUMBER = "+16813456223"
MY_PHONE_NUMBER = "+916351838207"
OWM_API_KEY = "69f04e4613056b159c2761a9d9e664d2"
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
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN, http_client=proxy_client)
    message = client.messages.create(
        body="Its going to rain today. Remember to bring an Umbrella!",
        from_=TWILIO_PHONE_NUMBER,
        to=MY_PHONE_NUMBER,
        force_delivery=True
    )
    print(message.status)

if __name__ == '__main__':
    print("")
