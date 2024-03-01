import requests
from twilio.rest import Client

OMW_ENDPOINT = "http://api.openweathermap.org/data/2.5/forecast"
API_KEY = "OPEN_WEATHER_API_KEY"

TWILIO_ACCOUNT = "TWILIO_ACCOUNT_ID"
TWILIO_TOKEN = "TWILIO_AUTH_TOKEN"


weather_params = {
    "lat": 33.518589,
    "lon": -86.810356,
    "appid": API_KEY,
    "cnt": 4
}

response = requests.get(OMW_ENDPOINT, params=weather_params)
response.raise_for_status()

weather_data = response.json()

rainy_weather = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        rainy_weather = True

if rainy_weather:
    print("Sending text message")
    client = Client(TWILIO_ACCOUNT, TWILIO_TOKEN)
    message = client.messages.create(body="It's going to rain today. Bring an umbrella",
                                     from_="+18555212027",
                                     to="+17325462483")
