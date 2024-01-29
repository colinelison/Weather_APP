# Weather_APP
Project for experimentation with OpenWeatherMap API

## How to Run
> [!NOTE]
> If your API call limit for the day has been reached, then the script will return an error
1. Ensure python is installed
   - Ran with version 3.12.1
2. Ensure modules/libraries are installed
   - `pip install -r requirements.txt`
3. Subscribe to One Call API 3.0 openweathermap and get your API key
4. Create file "config.py" with contents:
   - `API_KEY="<YOUR_API_KEY_GOES_HERE>"`
5. run `<YOUR_PYTHON_PATH> main.py`

## Environment Info

### `uname -srm`
MINGW64_NT-10.0-22621 3.3.6-341.x86_64 x86_64

### `python --version`
Python 3.12.1
