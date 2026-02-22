# Ingesting Bangalore city weather from weather API into Raw file 
import requests
import json
import os

API_KEY = "your_api_key_here" # You can paste your weather API here, I have personally used https://openweathermap.org/ to generate the API

CITY = "Bangalore"

URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}"

response = requests.get(URL)

data = response.json()

os.makedirs("../data/raw", exist_ok=True)

with open("../data/raw/weather_data.json", "w") as file:
    json.dump(data, file, indent=4)

print("Weather data successfully ingested!")
