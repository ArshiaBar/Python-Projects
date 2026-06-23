import requests
import os
from datetime import datetime,timedelta
from twilio.rest import Client

Loc='YTO'
client = Client(os.environ["AccountSid"], os.environ["AuthTok"])

sheetsdata=requests.get(os.environ['Sheety'],headers={'Authorization':os.environ['Token']}).json()

accesstoken=requests.post('https://test.api.amadeus.com/v1/security/oauth2/token',data={'grant_type':'client_credentials','client_id':os.environ['FlyAPIK'],'client_secret':os.environ['FlySec']},headers={'Content-Type':'application/x-www-form-urlencoded'}).json()['access_token']

#filling iata s
'''
for _ in sheetsdata['prices']:

    iata=requests.get("https://test.api.amadeus.com/v1/reference-data/locations/cities",params={'keyword':_['city']},headers={'Authorization':f'Bearer {accesstoken}'}).json()['data'][0]['iataCode']

    requests.put(f'{os.environ["Sheety"]}/{_["id"]}',json={"price":{"iataCode":iata}},headers={'Authorization':os.environ['Token']})

sheetsdata=requests.get(os.environ['Sheety'],headers={'Authorization':os.environ['Token']}).json()
'''

in7days=datetime.now()+timedelta(7)

for _ in sheetsdata['prices']:
    price=float(requests.get("https://test.api.amadeus.com/v2/shopping/flight-offers",params={'originLocationCode':Loc,'destinationLocationCode':_["iataCode"],'departureDate':in7days.strftime("%Y-%m-%d"),'adults':1,'currencyCode':'CAD'},headers={'Authorization':f'Bearer {accesstoken}'}).json()['data'][0]['price']['grandTotal'])
    print(price)
    if price < _['suggestedPrice']:
        client.messages.create(from_="+15706956847",to="+16477036685",body=f"Flight deal: ${price} CAD flying from {Loc} to {_['iataCode']} a week from now.")