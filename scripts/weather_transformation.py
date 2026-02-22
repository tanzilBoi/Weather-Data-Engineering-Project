# Transforming raw JSON data to CSV using Pyspark
import json
import pandas as pd
import os

with open("../data/raw/weather_data.json") as file:
    data = json.load(file)

city = data["name"]
temperature = data["main"]["temp"]
humidity = data["main"]["humidity"]
weather = data["weather"][0]["main"]
country = data["sys"]["country"]

df = pd.DataFrame({
    "City": [city],
    "Temperature": [temperature],
    "Humidity": [humidity],
    "Weather": [weather],
    "Country": [country]
})

os.makedirs("../data/processed", exist_ok=True)

df.to_csv("../data/processed/weather_processed.csv", index=False)

print("Data successfully transformed!")
