import requests

# Cluj Napoca's coordinates
MY_LAT = "46.770920"
MY_LON = "23.589920"


API_KEY = "8a580adf2603d3c102f664be261aac74"
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"

weather_params = {
    "lat": MY_LAT,
    "lon": MY_LON,
    "appid": API_KEY,
    "exclude": "current,minutely,daily"
}

weather_raw = requests.get(OWM_Endpoint, params=weather_params)

# if error occured
weather_raw.raise_for_status()

weather_json = weather_raw.json()

weather_for_12_hours = weather_json["hourly"][:12]

will_rain = False
for hour_data in weather_for_12_hours:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print(f"Don't forget your umbrella! It will rain today!")
else:
    print("No rain today")
