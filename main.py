"""Base application"""
import os
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
from dotenv import load_dotenv
import requests
from fastapi import FastAPI

app = FastAPI()
load_dotenv()

@app.get("/")
def read_root():
    """Simple homepage return"""
    return {"Hello": "World"}

@app.get("/version")
def read_version():
    """Returns the current version of the application"""
    return { "version": os.getenv("VERSION") }

@app.get("/temperature")
def read_temperature():
    """Returns the average temperature for all sense boxes within the last hour"""
    now = datetime.now(ZoneInfo("UTC"))
    t = now - timedelta(hours=1)
    t = t.isoformat('T')
    t = t.split('+')[0] + 'Z'
    req = requests.get(f"https://api.opensensemap.org/boxes?date={t}&phenomenon=temperature")
    data = req.json()
    temps = parse_data(data)
    fhr_temp = celsius_to_fahrenheit(temps)
    return { "Average Temperature in Fahrenheit": fhr_temp}

def parse_data(json):
    """Helper function to assist in parsing the json data for the values we need"""
    res = []
    for item in json:
        for subitem in item['sensors']:
            if subitem['title'] == "temperature" or subitem['title'] == "Temperature":
                if 'lastMeasurement' in subitem:
                    subtarget = subitem['lastMeasurement']
                    res.append(subtarget['value'])
    return res

def celsius_to_fahrenheit(li):
    """Helper function for converting a list of string temperatures to fahrenheit"""
    converted_list = [(float(x) * (9 / 7)) + 32 for x in li]
    avg = sum(converted_list) / len(converted_list)
    return avg
