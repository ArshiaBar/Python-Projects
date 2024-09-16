import datetime
import requests
import smtplib
import time
import os

while True:
    now=datetime.datetime.now()
    nsecs=now.hour*60*60+now.minute*60+now.second

    #my loc
    #https://www.latlong.net/
    #latitude=43.795430
    #longitude=-79.337530
    #https://www.php.net/manual/en/timezones.php
    #tzid=Canada/Eastern
    latitude=float(input("latitude? (for example 43.795430): "))
    longitude=float(input("longitude? (for example -79.337530): "))
    tzid=input("time zone id? (for example Canada/Eastern): ")

    #response=requests.get("https://api.sunrise-sunset.org/json",params={"lat":latitude,"lng":longitude})
    #response=requests.get("https://api.sunrise-sunset.org/json?lat=43.795430&lng=-79.337530")
    response=requests.get(f"https://api.sunrise-sunset.org/json?lat={latitude}&lng={longitude}&tzid={tzid}&formatted=0")
    response.raise_for_status()
    print(response.json())

    #west & east of greenwich
    if longitude<0:
        sign='-'
    elif longitude>=0:
        sign='+'

    sunrise=response.json()['results']['sunrise'].split('T')[1].split(sign)[0].split(':')
    sunset=response.json()['results']['sunset'].split('T')[1].split(sign)[0].split(':')

    srsecs=int(sunrise[0])*60*60+int(sunrise[1])*60+int(sunrise[2])
    stsecs=int(sunset[0])*60*60+int(sunset[1])*60+int(sunset[2])

    response=requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    print(response.json())

    iss_lat=float(response.json()['iss_position']['latitude'])
    iss_lng=float(response.json()['iss_position']['longitude'])

    if latitude-10<=iss_lat <=latitude+10 and longitude-10<=iss_lng<=longitude+10 \
            and nsecs not in range(srsecs,stsecs+1):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login("arshia.b.2014@gmail.com",os.environ["PAS"])
            connection.sendmail("arshia.b.2014@gmail.com","arshia.b.2014@gmail.com",
                                "Subject:ISS available\nLook up in the sky")

    time.sleep(60)