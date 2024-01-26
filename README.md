# Weather_API_App
Project for experimentation with OpenWeatherMap API

## How to Run
> [!NOTE]
> If your API call limit for the day has been reached, then the script will return an error
1. Ensure python is installed
   - Ran with version 3.12.1
2. Ensure modules/libraries are installed
   - `pip install geopy`
   - `pip install requests`
   - `pip install tzdata`
3. Subscribe to One Call API 3.0 openweathermap and get your API key
4. Create file "config.py" with contents:
   - `API_KEY="<YOUR_API_KEY_GOES_HERE>"`
5. run `<YOUR_PYTHON_PATH> main.py`

## Dependencies

### `uname -srm`
MINGW64_NT-10.0-22621 3.3.6-341.x86_64 x86_64

### `pip freeze`
certifi==2023.11.17 <br />
charset-normalizer==3.3.2 <br />
docopt==0.6.2 <br />
geographiclib==2.0 <br />
geopy==2.4.1 <br />
idna==3.6 <br />
pipreqs==0.4.13 <br />
requests==2.31.0 <br />
tzdata==2023.4 <br />
urllib3==2.1.0 <br />
yarg==0.1.9 <br />

### `pipreqs .`

geopy==2.4.1 <br />
Requests==2.31.0 <br />

### `python --version`
Python 3.12.1
