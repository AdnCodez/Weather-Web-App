# from django.views.generic import TemplateView
from django.shortcuts import render
import requests
import json
import math
import datetime


def fer_to_cel(value):
  result = (value - 32)/1.8000
  return round(result)
def mph_to_kph(value):
  result = value *  1.609344
  return round(float("%.2f" % result))
def epoch_to_human(value):
    result = '' + datetime.datetime.fromtimestamp(value).strftime('%A')[:3]
    result += ', ' + datetime.datetime.fromtimestamp(value).strftime('%d')
    result += ' ' + datetime.datetime.fromtimestamp(value).strftime('%B')
    result += ' ' + datetime.datetime.fromtimestamp(value).strftime('%Y')
    return result
def get_location():
  headers = {
    'Accept': 'application/json'
  }
  KEY = '3f55b07b200471d3ee97ce323483420208527f68fb6d3f0e57df3db5'
  response = requests.get('https://api.ipdata.co?api-key={}'.format(KEY), headers=headers)

  response_body = response.json()
  latitude = response_body['latitude']
  longitude = response_body['longitude']
  city = response_body['city']
  return latitude, longitude, city

def index(request):
    API_Secret_key = "becbbc15c724474fdab20f1d500ac33b"
    API_URL = "https://api.darksky.net/forecast/{0}/{1},{2}"
    resp = requests.get(API_URL.format(API_Secret_key,get_location()[0] ,get_location()[1]))
    # # print(resp)
    data = resp.json()
    # TIME
    current_time = data["currently"]['time']
    current_time_human = epoch_to_human(current_time)
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

    weather = {
      'time': current_time_human,
      'city': get_location()[2],
      'temp_F': current_temp_inF,
      'temp_C': current_temp_inC,
      'wind_kph': current_wind_speed_kph,
      'wind_mph': current_wind_speed_mph,
      'summary_short': current_summary,
      'summary_extended': summary,
      'temp_high_F': temp_high_inF,
      'temp_low_F': temp_low_inF,
      'temp_high_C': temp_high_inC,
      'temp_low_C': temp_low_inC,
    }
    context = {'weather' : weather}

    return render(request, 'Date/index.html', context) #returns the index.html template
