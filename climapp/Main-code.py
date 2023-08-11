from datetime import datetime
import requests

def get_weather(api_key, city):
    base_url = ""
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric" 
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    return data

def main():
    api_key = "" #your weather API.
    city = input("Name the city: ")
    local_dt = datetime.now()
    hour = local_dt.strftime("%H:%M")


    
    weather_data = get_weather(api_key, city)
    if "main" in weather_data:
        temperature = weather_data["main"]["temp"]
        description = weather_data["weather"][0]["description"]
        print(f"temperature in {city}: {temperature:.2f}°C at {hour}")  
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