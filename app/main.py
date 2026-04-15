# flake8: noqa: N806
import os
import requests
from dotenv import load_dotenv


def get_weather() -> None:
    load_dotenv()
    API_KEY = os.getenv("API_KEY")
    FILTERING = "Paris"
    URL = (f"http://api.weatherapi.com/v1/"
           f"current.json?key={API_KEY}&q={FILTERING}")
    if not API_KEY:
        print("API_KEY not set")
    else:
        response = requests.get(URL)
        if response.status_code == 200:
            data = response.json()
            city = data["location"]["name"]
            country = data["location"]["country"]
            day_time = data["location"]["localtime"]
            temperature = data["current"]["temp_c"]
            type_weather = data["current"]["condition"]["text"]
            print("Performing request to Weather API for city Paris...")
            print(
                f"{city}/ {country} {day_time} "
                f"Weather: {temperature} Celsius, {type_weather}"
            )
        else:
            print("Error code:", response.status_code, response.text)


if __name__ == "__main__":
    get_weather()
