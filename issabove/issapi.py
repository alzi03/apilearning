import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 40.744630  # Your latitude
MY_LONG = -73.881710  # Your longitude


def coordinates():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    print(data)
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG:
        return True
    return False

def suncycle():
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
    hour = int(str(time_now).split(' ')[1].split(':')[0])
    if hour >= sunset or hour <= sunrise:
        return True
    return False

EMAIL = 'alam.zishan534@gmail.com'
PASSWORD = 'GymUser646'
while True:
    time.sleep(60)
    if suncycle() and coordinates():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,
            msg='Subject:ISS Above\n\nThe ISS can be seen from your position'

        )






#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



