import requests
from datetime import datetime

#response = requests.get(url='http://api.open-notify.org/iss-now.json')
#
#response.raise_for_status()
#
#
#longitude = response.json()["iss_position"]["longitude"]
#latitude = response.json()["iss_position"]["latitude"]
#
#iss_position = (latitude, longitude)
#print(iss_position)

current_time = datetime.now().hour
print(current_time)
parameters = {
    'lat':39.470242,
    'lng':-0.376800,
    'formatted':0
}
response = requests.get("https://api.sunrise-sunset.org/json",params=parameters)
response.raise_for_status()
data = response.json()
print(data)

sunrise = data['results']['sunrise'].split('T')[1].split(':')[0]
sunset = data['results']['sunset'].split('T')[1].split(':')[0]
print(sunrise)
print(sunset)
