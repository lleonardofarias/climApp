<h1>Climapp</h1>

> Status: Developing ⚠

### Climapp is an application that uses an API to provide temperature and climate information for a specific location.

## What is a Climate API?

A Climate API (Application Programming Interface) is a tool that allows different applications, like Climapp, to interact with a weather data service. It's like a bridge that enables the app to request weather-related information from the service and receive it in a format that the app can understand and display. Like OpenWeatherMap API, Weatherbit API, and others.

## How to run the application?

1. **Get your API Key:**
   - Go to the Climate API website. 
   - Sign up or log in to get access. 
   - Look for an option to generate an API Key. It's like a password that the app uses to talk to the API.

2. **Put your API Key in the app:**
   - Once you have your API Key, go to the "config.ini" file.
   - Inside the "config.ini" file, you i'll see the section "[Weather]".
   - You'll see a line that says "appid = _____". Replace the blank with your actual API Key.

Example:
```ini
 [config.ini]

 [Weather]
 appid = "YOUR_API_KEY_HERE"



