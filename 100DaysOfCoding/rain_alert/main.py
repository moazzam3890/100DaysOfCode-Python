import requests
import os
from twilio.rest import Client

my_key = os.environ.get("OWM_KEY")
params = {
    "lat": 25.014373,
    "lon": 67.126956,
    "appid": my_key,
    "exclude": "current,minutely,daily,alerts",
}
account_sid = "AC0873bc0c362d04c3c5d2c22cc217f5c4"
auth_token = os.environ.get("TWILIO_AUTH_KEY")

response = requests.get(
    url="https://api.openweathermap.org/data/2.5/onecall",
    params=params,
)

response.raise_for_status()
print(response)

data = response.json()
hourly_data = data["hourly"][0:12]
hourly_data_id = [x["weather"][0]["id"] for x in hourly_data]
print(hourly_data_id)

will_rain = False

for value in hourly_data_id:
    if value < 600:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Wear Casual cloths for Office.",
        from_="Twillio Number",
        to="Your Number"
    )
    print(message.status)
else:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's not going to rain today.",
        from_="Twillio Number",
        to="Your Number"
    )
    print(message.status)

