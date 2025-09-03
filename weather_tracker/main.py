import sys
from weather_utils import fetch_weather

def main():
    print("Welcome to the Weather Tracker!")
    print("Enter city names one by one. Type 'done' to finish.")

    cities_to_track = []
    while True:
        city_name = input("City: ").strip()
        if city_name.lower() == 'done':
            if not cities_to_track:
                print("No cities entered. Exiting.")
                sys.exit(0)
            break
        elif city_name:
            cities_to_track.append(city_name)
    
    print("\nFetching weather data...")
    weather_reports = []
    for city in cities_to_track:
        weather_obj = fetch_weather(city)
        if weather_obj:
            weather_reports.append(weather_obj)

    if weather_reports:
        print("\nWeather Report:")
        for report in weather_reports:
            print(report)
            print("-" * 80)
    else:
        print("\nNo weather data could be fetched for the specified cities.")

if __name__ == "__main__":
    main()
