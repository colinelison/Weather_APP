import config
import PySimpleGUI as sg
from zoneinfo import ZoneInfo
from geopy.geocoders import Nominatim
import time
import requests
import datetime

def getInfo(LAT,LON):
    # Set unit of measurement to imperial
    UNITS = "imperial"

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

        # Another way of getting formatted time using time (seems more flexible)
        LOCAL_TIME_2 = time.strftime("%A %B %d, %Y @ %I:%M:%S %p %z", time.localtime(TIME_UTC_EPOCH_SECONDS))

        # Use the geopy module to convert latitude and longitude into a location
        # A dictionary is returned with location information
        GEOLOCATOR = Nominatim(user_agent="Elison_application")
        LOCATION = GEOLOCATOR.reverse(LAT+","+LON, language='en')

        localeStr = ""

        # Check that there is an address associated with the coordinates
        if (LOCATION is not None):
            GEO_DICT = LOCATION.raw['address']
            localeStr = "({}) ".format(
                    ((GEO_DICT['city'] + ", ") if ('city' in GEO_DICT) else "")+
                    ((GEO_DICT['state'] + " ") if ('state' in GEO_DICT) else "")+
                    (("in " + GEO_DICT['country']) if ('country' in GEO_DICT) else "")
                    )
        
        displayStr = "The current temperature at {0} Latitude by {1} Longitude {2}is {3} degrees fahrenheit on {4} MDT".format(
            LAT,
            LON,
            localeStr,
            WEATHER_DICT['current']['temp'],
            LOCAL_TIME_2
            )
    
    return displayStr

sg.theme('BrownBlue')
sg.Titlebar("Elison Weather Application")

layout = [
    [
        sg.Text("Please input a Latitude coordinate (decimal degrees [-90,90])"),
        sg.In(size=(10,1),enable_events=True,key='LAT-INPUT-FIELD'),
    ],
    [
        sg.Text("Please input a Longitude coordinate (decimal degrees [-180,180])"),
        sg.In(size=(10,1),enable_events=True,key='LON-INPUT-FIELD'),
    ],
    [
        sg.Submit(key='SUBMIT-BUTTON',),
    ],
    [
        sg.Text("Please submit new coordinates", visible=False, key='SAME-COORDINATES-TEXT'),
    ],
    [
        sg.Text(visible=False, auto_size_text=True, key='OUTPUT-TEXT',background_color="grey",text_color="white"),
    ]
]

window = sg.Window("Weather Application", layout, size=(1500,200))

previousEntry = ""

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    
    if event == 'SUBMIT-BUTTON':

        LAT = values['LAT-INPUT-FIELD']
        LON = values['LON-INPUT-FIELD']

        if ((LAT+LON) == previousEntry):
            window['SAME-COORDINATES-TEXT'].update(visible=True)
            continue

        window['SAME-COORDINATES-TEXT'].update(visible=False)

        displayStr = getInfo(LAT,LON)
        
        window['OUTPUT-TEXT'].update(displayStr,visible=True)

        previousEntry = LAT+LON

