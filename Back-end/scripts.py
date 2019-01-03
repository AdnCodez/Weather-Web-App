from django.shortcuts import render
import requests
import json
import math
import datetime


# ls = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]

def weather_api(lat, lon, epoch_time):
  dark_sky_URL = "https://api.darksky.net/forecast/becbbc15c724474fdab20f1d500ac33b/{0},{1},{2}?units=si".format(lat, lon, epoch_time)
  response = requests.get(dark_sky_URL)
  weather_api_data = response.json()
  return weather_api_data

def epoch_time():
  return int(datetime.datetime.now().timestamp())

def epoch_time_to_human(value):
    result = '' + datetime.datetime.fromtimestamp(value).strftime('%A')[:3]
    result += ', ' + datetime.datetime.fromtimestamp(value).strftime('%d')
    result += ' ' + datetime.datetime.fromtimestamp(value).strftime('%B')
    result += ' ' + datetime.datetime.fromtimestamp(value).strftime('%Y')
    return result

def epoch_time_day_name(value):
    day_name = datetime.datetime.fromtimestamp(value).strftime('%A')[:3]
    return day_name
print(epoch_time_day_name(epoch_time()))

def get_location():
  headers = {'Accept': 'application/json'}
  KEY = '3f55b07b200471d3ee97ce323483420208527f68fb6d3f0e57df3db5'
  resp = requests.get('https://api.ipdata.co?api-key={}'.format(KEY), headers=headers)
  response_body = resp.json()
  latitude = response_body['latitude']
  longitude = response_body['longitude']
  city = response_body['city']
  return latitude, longitude, city

def index(request):
    # TIME
    current_time = epoch_time()
    current_time_human = epoch_time_to_human(current_time)
    # CURRENT TEMPERATURE  °C MORE PRECISE
    current_temp_inC = round(weather_api(get_location()[0], get_location()[1], epoch_time())["currently"]["temperature"])
    # CURRENT SUMMARY (SHORT)
    current_summary = weather_api(get_location()[0], get_location()[1], epoch_time())["currently"]["summary"]
    # CURRENT WIND SPEED Meters per second.
    current_wind_speed_mps = round(weather_api(get_location()[0], get_location()[1], epoch_time())["currently"]["windSpeed"])
    # SUMMARY EXTENDED
    summary = weather_api(get_location()[0], get_location()[1], epoch_time())["daily"]["data"][0]["summary"]
    # DAILY HIGH TEMPERATURE AND LOW TEMPERATURE °C
    temp_high_inC = round(weather_api(get_location()[0], get_location()[1], epoch_time())["daily"]["data"][0]["temperatureHigh"])
    temp_low_inC = round(weather_api(get_location()[0], get_location()[1], epoch_time())["daily"]["data"][0]["temperatureLow"])
    # ICON OF THE CURRENT TEMP
    icon = weather_api(get_location()[0], get_location()[1], epoch_time())["currently"]["icon"]
    if '-' in icon:
      icon = ''.join(icon.split('-')[:-1])
    else:
      icon

    weather = {
      'time': current_time_human,
      'city': get_location()[2],
      'temp_C': current_temp_inC,
      'wind_mps': current_wind_speed_mps,
      'summary_short': current_summary,
      'summary_extended': summary,
      'temp_high_C': temp_high_inC,
      'temp_low_C': temp_low_inC,
      'icon': icon,
      'day_name': epoch_time_day_name(),
    }
    context = {'weather' : weather}
    return render(request, 'Date/index.html', context) #returns the index.html template
