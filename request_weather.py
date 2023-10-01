from dotenv import load_dotenv
import os
import requests

load_dotenv(".env")
APIkey = os.environ.get("OpenWeatherAPI")


def get_weather_data(place, forecast_days, weather_option):
    city_name = place
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={APIkey}"
    response = requests.get(url)
    content = response.json()

    nr_values = forecast_days * 8
    weather = []
    nr_extracted_values = 0
    for day in content['list']:
        if nr_values > nr_extracted_values:
            match weather_option:
                case "Temperature":
                    temperature = day['main']['temp']
                    temperature = round(temperature / 10, 2)
                    weather.append(temperature)
                case "Sky":
                    sky = day['weather'][0]['description']
                    weather.append(sky)
            nr_extracted_values += 1
    return weather


if __name__ == "__main__":
    print(get_weather_data(place="Tokyo", forecast_days=5, weather_option="Temperature"))
