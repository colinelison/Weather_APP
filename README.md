# Weather_API_App
Project for experimentation with OpenWeatherMap API

> [!NOTE]
> If the API call limit for the day has been reached (1000) then the script won't work

## How to Run
1. Ensure python is installed
   - Ran with version 3.12.1
1. Ensure modules/libraries are installed
   - `pip install geopy`
   - `pip install requests`
   - `pip install tzdata`
2. Create file "config.py" with contents:
   - `API_KEY="<YOUR_API_KEY_GOES_HERE>"`
3. run `<YOUR_PYTHON_PATH> main.py`

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

Requests==2.31.0

### `python --version`
Python 3.12.1
