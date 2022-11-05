import time
import requests
from datetime import datetime
import smtplib

MY_EMAIL = 'franperezfolgado@outlook.com'
PASSWORD = 'placehodler'
SMTP = 'outlook.office365.com'


def send_email():
    print('sending email')
    try:
        with smtplib.SMTP(SMTP) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL, to_addrs='franciscoperezfolgado@gmail.com', msg='Subject:ISS location!\n\nTHE ISS IS IN YOUR CURRENT LOCATION')
    except smtplib.SMTPException:
        print('Error sending email')


def compare_position(your_pos: float, iss_pos: float) -> bool:
    range_max = your_pos+5
    range_min = your_pos-5
    return iss_pos > range_min and iss_pos < range_max


MY_LAT = 39.470242  # Your latitude
MY_LONG = -0.376800  # Your longitude
parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
while True:
    print('Checking ISS location')
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    response = requests.get(
        "https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    current_lat = compare_position(MY_LAT, iss_latitude)
    current_lng = compare_position(MY_LONG, iss_longitude)

    is_dark = time_now > sunset and time_now < sunrise


    
    if current_lat and current_lng and is_dark:
        send_email()
    
    time.sleep(60)