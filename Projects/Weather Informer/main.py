import requests
import os
from twilio.rest import Client

lat=43.759838
lon=-79.411209
api_key='2d24d15435fa53eb218f53d05b41fb53'
#api_key=os.environ.get("ForecastAPIKey")
api=f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&cnt=4&appid={api_key}'

response=requests.get(api)
response.raise_for_status()
weather_data=response.json()
print(weather_data)

data=[]
for _ in weather_data['list']:
    data.append(_['weather'][0]['description'])

account_sid = "AC103490a356ac883da37b8e5543265ddb"
auth_token = "13f492c5fc228b706d14a5cf6502e2c3"
#auth_token= os.environ.get("ForecastAuthToken")
client = Client(account_sid, auth_token)
message = client.messages.create(
    body=f"It's {data[0]} at 9AM, {data[1]} at 12PM, {data[2]} at 3PM, {data[3]} at 6PM. Your discretion is advised.",
    from_="+15706956847",
    to="+16477036685",
)

#whatsapp: https://console.twilio.com/us1/develop/sms/try-it-out/whatsapp-learn  #u need to connect ur whatsapp
#code:

"""
message = client.messages.create(
  from_="whatsapp:TWILIO_WHATSAPP_NUMBER",
  body="It's going to rain today. Remember to bring an umbrella",
  to="whatsapp:YOUR_TWILIO_VERIFIED_NUMBER"
)
"""

