from dotenv import load_dotenv
import os
import requests

load_dotenv(".env")
APIkey = os.environ.get("OpenWeatherAPI")


def get_weather_data(place, forecast_days=None, weather_option=None):
    city_name = place
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={APIkey}"
    response = requests.get(url)
    content = response.json()
    return content


if __name__ == "__main__":
    print(get_weather_data(place="Tokyo"))
