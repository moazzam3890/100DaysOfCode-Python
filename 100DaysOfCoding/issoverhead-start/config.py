import requests
from datetime import datetime

MY_LAT = 25.016551  # Your latitude
MY_LONG = 67.123186  # Your longitude


def iss_position():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.
    if (MY_LAT-5 < iss_latitude < MY_LAT+5) and (MY_LONG-5 < iss_longitude < MY_LONG+5):
        return True


def sunset_sunrise():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    hour_now = time_now.hour

    # If the ISS is close to my current position
    # and it is currently dark
    if sunset <= hour_now <= sunrise:
        return True
