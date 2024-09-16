import requests
from datetime import datetime
import os

#setting environment variable ex.
#os.environ['APPID']="f2422a3b"

'''
APP_ID = os.environ["APP_ID"] – raises exception if key does not exist
APP_ID = os.environ.get("APP_ID") – returns None if key does not exist
APP_ID = os.environ.get("APP_ID", “Message”) – returns “Message” if key does not exist
'''

res=requests.post("https://trackapi.nutritionix.com/v2/natural/exercise",json={"query":input("what exercises?"),"weight_kg":input("weight in kg?"),"height_cm":input("height in cm?"),"age":input("age?")},headers={"x-app-id":os.environ['APPID'], "x-app-key":os.environ['APIKEY']})
data=res.json()
#print(data)

#https://www.w3schools.com/python/python_datetime.asp
for _ in data['exercises']:
    dictt={
        "workout":{
            'date':datetime.now().strftime("%d/%m/%Y"),
            'time':datetime.now().strftime("%X"),
            'exercise': _['name'].title(),
            'calories':_['nf_calories']
        }
    }

    #no authentication
    #res=requests.post(os.environ['SheetEndpoint'],json=dictt)

    #basic authentication
    #res=requests.post("https://api.sheety.co/ae6ab9f56c54c13709f811e6eda6105d/copyOfMyWorkouts/workouts",json=dictt,auth=(os.environ['Username'],os.environ['Password']))

    #bearer token authentication
    res=requests.post("https://api.sheety.co/ae6ab9f56c54c13709f811e6eda6105d/copyOfMyWorkouts/workouts",json=dictt,headers={"Authorization": os.environ['BearerToken']})
