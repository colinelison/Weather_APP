import config

from zoneinfo import ZoneInfo
from geopy.geocoders import Nominatim
import time
import requests
import datetime

# Program to get weather data from a specific location based on latitude and longitude
if __name__ == '__main__':

    # Request coordinates from user
    LAT = input("Please input latitude (decimal degrees [-90,90]): ")
    LON = input("Please input longitude (decimal degrees [-180,180]): ")

    # Set unit of measurement to imperial
    UNITS = "imperial"

    # Build web API call
    url = "https://api.openweathermap.org/data/3.0/onecall?"
    url = url + "lat=" + LAT + "&lon=" + LON + "&units=" + UNITS + "&appid=" + config.API_KEY

    # Make call and get response
    RESPONSE = requests.get(url)

    # Deserialize JSON string into dictionary
    WEATHER_DICT = RESPONSE.json()

    # Check if there was an error
    if ('cod' in WEATHER_DICT.keys()):
        print("Error code {0}: {1}".format(WEATHER_DICT['cod'], WEATHER_DICT['message']))
        exit(1)
            
    # Get time in epoch seconds by accessing the value of the 'dt' key of the 'current' key of the returned dictionary
    TIME_UTC_EPOCH_SECONDS = int(WEATHER_DICT['current']['dt'])

    # One way of getting formatted time using datetime
    LOCAL_TIME = datetime.datetime.fromtimestamp(TIME_UTC_EPOCH_SECONDS, ZoneInfo("America/Denver"))

    # Another way of getting formatted time using time (seems more flexible)
    LOCAL_TIME_2 = time.strftime("%A %B %d, %Y @ %I:%M:%S %p %z", time.localtime(TIME_UTC_EPOCH_SECONDS))

    # Use the geopy module to convert latitude and longitude into a location
    # A dictionary is returned with location information
    GEOLOCATOR = Nominatim(user_agent="Elison_application")
    LOCATION = GEOLOCATOR.reverse(LAT+","+LON)
    GEO_DICT = LOCATION.raw['address']

    # Display info
    print("\n")
    print("The current temperature in {0}, {1} ({2}) is {3} degrees fahrenheit on {4} MDT".format
        (
        GEO_DICT['city'],
        GEO_DICT['state'],
        GEO_DICT['country'],
        WEATHER_DICT['current']['temp'],
        LOCAL_TIME_2
        ))
