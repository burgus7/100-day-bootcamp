import requests
from datetime import datetime
import time

MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude

# get current iss location
def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # check if your position is within +5 or -5 degrees of the ISS position.
    is_iss_close = False
    if abs(iss_latitude - MY_LAT) < 5 and abs(iss_longitude - MY_LONG) < 5:
        is_iss_close = True
    return is_iss_close

def is_night():
    # get sunrise and sunset
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

    time_now = str(datetime.now())
    this_hour = int(time_now.split(" ")[1].split(":")[0])

    if sunrise < this_hour and this_hour < sunset:
        return False
    else:
        return True

while True:
    time.sleep(60)
    if is_night() and is_iss_overhead():
        print("look up!") # TODO add emails with GCP
    else:
        print("iss not here yet")

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

#Your position is within +5 or -5 degrees of the ISS position.
