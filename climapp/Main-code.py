from datetime import datetime
import requests
from configparser import ConfigParser

config = ConfigParser()
config.read("config.ini")

def get_weather(api_key, city, units):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": units  # Use the units specified by the user
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    return data

def main():
    api_key = config.get('Weather', 'appid')
    city = input("Name the city: ")
    units = input("Select temperature units (C/F/K): ").lower()
    if units == "c":
        units = "metric"
    elif units == "f":
        units = "imperial"
    elif units == "k":
        units = "standard"
    else:
        print("Invalid units. Using default units.")
        units = config.get('Weather', 'units')

    local_dt = datetime.now()
    hour = local_dt.strftime("%H:%M")

    weather_data = get_weather(api_key, city, units)  # Provide the units argument here
    if "main" in weather_data:
        temperature = weather_data["main"]["temp"]
        description = weather_data["weather"][0]["description"]
        print(f"Temperature in {city}: {temperature:.2f} in the metric that you choose, at {hour}")
        print(f"Condition: {description}")
    else:
        print("Unable to get weather data")

def repeat():
    while True:
        run_again = input('Want to run again?: ').lower()
        if run_again == 'yes':
            main()
        elif run_again == 'no':
            break

if __name__ == "__main__":
    main()
    repeat()
