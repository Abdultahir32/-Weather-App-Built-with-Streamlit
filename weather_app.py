import streamlit as st
import requests
from datetime import datetime

API_KEY = "a9370266a18ceef8834921a0414571b8"
CURRENT_WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"
FORECAST_URL = "https://api.openweathermap.org/data/2.5/forecast"

def get_current_weather(city):
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(CURRENT_WEATHER_URL, params=params)
    return response.json()

def get_forecast(city):
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(FORECAST_URL, params=params)
    return response.json()

def display_current_weather(data):
    st.subheader("🌤️ Current Weather")
    weather = data["weather"][0]["description"].title()
    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]
    st.write(f"**Description:** {weather}")
    st.write(f"**Temperature:** {temp}°C")
    st.write(f"**Humidity:** {humidity}%")
    st.write(f"**Wind Speed:** {wind_speed} m/s")

def display_forecast(data):
    st.subheader("📅 5-Day Forecast (3-hour intervals)")
    for item in data["list"]:
        dt = datetime.fromtimestamp(item["dt"])
        description = item["weather"][0]["description"].title()
        temp = item["main"]["temp"]
        humidity = item["main"]["humidity"]
        wind = item["wind"]["speed"]
        st.markdown(f"""
        **{dt.strftime('%A, %d %b %Y %H:%M')}**
        - 🌡️ Temp: {temp}°C
        - 💧 Humidity: {humidity}%
        - 💨 Wind: {wind} m/s
        - 🔸 {description}
        """)

st.title("🌍 Weather App with 5-Day Forecast")
city = st.text_input("Enter a city name", "Delhi")

if st.button("Get Weather"):
    weather_data = get_current_weather(city)
    forecast_data = get_forecast(city)
    if weather_data.get("cod") == 200 and forecast_data.get("cod") == "200":
        display_current_weather(weather_data)
        display_forecast(forecast_data)
    else:
        st.error("City not found or API error.")

