<h1>Climapp</h1>

> Status: Developing ⚠

### Climapp is an application that uses an API to provide temperature and climate information for a specific location.

## What is a Climate API?

A Climate API (Application Programming Interface) is a tool that allows different applications, like Climapp, to interact with a weather data service. It's like a bridge that enables the app to request weather-related information from the service and receive it in a format that the app can understand and display. Like OpenWeatherMap API, Weatherbit API, and others.

## What is an API Key?

An API Key is like a digital keycard:
- It grants your app access to specific data from an API.
- Just as you need a keycard to enter a building, your app needs an API Key to access data.
- It's a secret code that ensures only authorized users can use the API.

For Climapp:
- Your API Key from the Climate API is your app's keycard.
- It's inserted into the app's configuration to fetch weather data.
- Treat it like a password: keep it private for security.


## How to run the application?

1. **Get your API Key:**
   - Go to the Climate API website. It can be anyone (as long as you get the API_KEY, if I don't know any, just search for "climate API" or see the examples cited in the text above)
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
```
3. **Runs the application**

   - Navigate to the Climapp directory using your terminal or command prompt.
   - Run the "Main-code.py" file by typing the following command and pressing Enter:
```
python Main-code.py
```
If you use Windows you might use a command like this:
```
python.exe Main-code.py
```




