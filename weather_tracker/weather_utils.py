import requests
from weather_module import Weather
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")

BASE_URL = "http://api.weatherapi.com/v1/current.json"

def fetch_weather(city):
    if API_KEY == "YOUR_API_KEY":
        print("Error: Please replace 'YOUR_API_KEY' in weather_utils.py with your API key.")
        return None

    params = {
        'key': API_KEY,
        'q': city,
        'aqi': 'no'
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        response.raise_for_status() 
        data = response.json()

        if "error" in data:
            print(f"Error for {city}: {data['error']['message']}")
            return None

        location = data['location']
        current = data['current']

        weather_obj = Weather(
            city=location['name'],
            temperature=current['temp_c'],
            condition=current['condition']['text'],
            humidity=current['humidity'],
            wind_speed=current['wind_kph'],
            last_updated=current['last_updated']
        )
        return weather_obj

    except requests.exceptions.RequestException as e:
        print(f"Network error for {city}: {e}")
    except Exception as e:
        print(f"An unexpected error occurred for {city}: {e}")
    
    return None
