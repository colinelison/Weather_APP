import config

from zoneinfo import ZoneInfo
from geopy.geocoders import Nominatim
import time
import requests
import datetime

# Program to get weather data from a specific location based on latitude and longitude
if __name__ == '__main__':


    lat = input("Please input latitude (decimal degrees [-90,90]): ")
    lon = input("Please input longitude (decimal degrees [-180,180]): ")

    units = "imperial"
    URL = "https://api.openweathermap.org/data/3.0/onecall?"
    URL = URL + "lat=" + lat + "&lon=" + lon + "&units=" + units + "&appid=" + config.API_KEY

    response = requests.get(URL)
    weatherDict = response.json()

    if ('cod' in weatherDict.keys()):
        print("Error code {0}: {1}".format(weatherDict['cod'], weatherDict['message']))
        exit(1)
            
    time_utc_epoch_seconds = int(weatherDict['current']['dt'])

    # one way of doing it using datetime
    local_time = datetime.datetime.fromtimestamp(time_utc_epoch_seconds, ZoneInfo("America/Denver"))

    # another way of doing it using time (seems more flexible)
    local_time_2 = time.strftime("%A %B %d, %Y @ %I:%M:%S %p %z", time.localtime(time_utc_epoch_seconds))

    geolocator = Nominatim(user_agent="Elison_application")
    location = geolocator.reverse(lat+","+lon)
    geoDict = location.raw['address']

    print("\n")
    print("The current temperature in {0}, {1} ({2}) is {3} degrees fahrenheit on {4} MDT".format(geoDict['city'], geoDict['state'], geoDict['country'], weatherDict['current']['temp'], local_time_2))
