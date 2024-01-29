import config
import PySimpleGUI as sg
from zoneinfo import ZoneInfo
from geopy.geocoders import Nominatim
import time
import requests
import datetime

# Script to get weather data from a specific location based on latitude and longitude

sg.theme('BluePurple')

layout = [
    [
        sg.Text("Please input a Latitude coordinate (decimal degrees [-90,90])"),
        sg.In(size=(10,1),enable_events=True,key='LAT-INPUT-FIELD'),
        sg.Text("Please input a Longitude coordinate (decimal degrees [-180,180])"),
        sg.In(size=(10,1),enable_events=True,key='LON-INPUT-FIELD'),
    ],
    [
        sg.Submit(key='SUBMIT-BUTTON'),
    ],
    [
        sg.Text(visible=False, key='OUTPUT-TEXT'),
    ]
]

window = sg.Window("Weather Application", layout)

recentEntry = ""

# # Request coordinates from user
# LAT = input("Please input latitude (decimal degrees [-90,90]): ")
# LON = input("Please input longitude (decimal degrees [-180,180]): ")

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    
    if event == 'SUBMIT-BUTTON':

        # Set unit of measurement to imperial
        UNITS = "imperial"

        LAT = values['LAT-INPUT-FIELD']
        LON = values['LON-INPUT-FIELD']

        # Build web API call
        url = "https://api.openweathermap.org/data/3.0/onecall?"
        url = url + "lat=" + LAT + "&lon=" + LON + "&units=" + UNITS + "&appid=" + config.API_KEY

        # Make call and get response
        RESPONSE = requests.get(url)

        # Deserialize JSON into dictionary
        WEATHER_DICT = RESPONSE.json()

        displayStr = ""
        # Check if there was an error
        if ('cod' in WEATHER_DICT.keys()):
            displayStr = "Error code {0}: {1}".format(WEATHER_DICT['cod'], WEATHER_DICT['message'])
        else:                
            # Get time in epoch seconds by accessing the value of the 'dt' key of the 'current' key of the returned dictionary
            TIME_UTC_EPOCH_SECONDS = int(WEATHER_DICT['current']['dt'])

            # One way of getting formatted time using datetime
            LOCAL_TIME = datetime.datetime.fromtimestamp(TIME_UTC_EPOCH_SECONDS, ZoneInfo("America/Denver"))

            # Another way of getting formatted time using time (seems more flexible)
            LOCAL_TIME_2 = time.strftime("%A %B %d, %Y @ %I:%M:%S %p %z", time.localtime(TIME_UTC_EPOCH_SECONDS))

            # Use the geopy module to convert latitude and longitude into a location
            # A dictionary is returned with location information
            GEOLOCATOR = Nominatim(user_agent="Elison_application")
            LOCATION = GEOLOCATOR.reverse(LAT+","+LON, language='en')


            try:
                GEO_DICT = LOCATION.raw['address']
                displayStr = "The current temperature at {0} Latitude by {1} Longitude ({2} {3} ({4})) is {5} degrees fahrenheit on {6} MDT".format(
                    LAT,
                    LON,
                    (GEO_DICT['city'] if ('city' in GEO_DICT) else ""),
                    (GEO_DICT['state'] if ('state' in GEO_DICT) else ""),
                    (GEO_DICT['country'] if ('country' in GEO_DICT) else ""),
                    WEATHER_DICT['current']['temp'],
                    LOCAL_TIME_2
                    )
            # If coordinates do not point to an address (like somewhere in the middle of the ocean)
            except AttributeError:
                displayStr = "The current temperature at {0} Latitude by {1} Longitude is {2} degrees fahrenheit on {3} MDT".format(
                    LAT,
                    LON,
                    WEATHER_DICT['current']['temp'],
                    LOCAL_TIME_2
                    )
        window['OUTPUT-TEXT'].update(displayStr,visible=True)

