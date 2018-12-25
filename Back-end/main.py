import requests
import json
import math


def fer_to_cel(value):
  result = (value - 32)/1.8000
  return round(result)
def mph_to_kph(value):
  result = value *  1.609344
  return round(float("%.2f" % result))

API_Secret_key = "becbbc15c724474fdab20f1d500ac33b"
API_URL = "https://api.darksky.net/forecast/{0}/{1},{2}"
# headers = {'Content-Type': 'application/json','Authorization': 'Bearer {0}'.format(API_Secret_key)}
# resp = requests.get(API_URL, headers=headers)

resp = requests.get(API_URL.format(API_Secret_key,34.26101,-6.5802))
# print(resp)
data = resp.json()

# TIME
current_time = data["currently"]['time']
# CURRENT TEMPERATURE  °C & °F MORE PRECISE
current_temp_inF = round(data["currently"]["temperature"])
current_temp_inC = fer_to_cel(current_temp_inF)
# SUMMARY SHORT
current_summary = data["currently"]["summary"]
# WIND SPEED MPH KPH
current_wind_speed_mph = data["currently"]["windSpeed"]
current_wind_speed_kph = mph_to_kph(data["currently"]["windSpeed"])
# SUMMARY EXTENDED
summary = data["daily"]["summary"]
# DAILY HIGH TEMPERATURE AND LOW TEMPERATURE °C & °F
temp_high_inF = round(data["daily"]["data"][0]["temperatureHigh"])
temp_high_inC = fer_to_cel(temp_high_inF)
temp_low_inF = round(data["daily"]["data"][0]["temperatureLow"])
temp_low_inC = fer_to_cel(temp_low_inF)
