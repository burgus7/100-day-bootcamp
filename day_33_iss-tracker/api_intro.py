import requests
from datetime import datetime

response = requests.get(url="http://api.open-notify.org/iss-now.json")

# status codes: 1XX - hold on; 2xx - success; 3xx - ; 4xx - you screwed up; 5xx - i (server) screwed up
response.raise_for_status() # this will give the error

data = response.json()
print(data)

longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]
iss_position = (longitude, latitude)

print(iss_position)

# TODO - remember to do day 30-32!
# TODO - need to add email using gcp


# check if it is night (if day, iss wont be visible)
MY_LAT = 100
MY_LNG = 100
parameters = {"lat": MY_LAT,
              "lng": MY_LNG,
              "formatted": 0
             }
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

sunrise = data["results"]["sunrise"].split("T")[1].split(":")
sunset = data["results"]["sunset"].split("T")[1].split(":")


time_now = datetime.now()
print(sunrise)