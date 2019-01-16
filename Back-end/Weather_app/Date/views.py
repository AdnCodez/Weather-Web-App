# from django.views.generic import TemplateView
from django.shortcuts import render
import requests
import json
import math
import datetime

from .forms import CityForm
from .city import fun

# ls = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]


#**************************************************************************************
def weather_api(lat, lon, epoch_time):
    dark_sky_URL = "https://api.darksky.net/forecast/becbbc15c724474fdab20f1d500ac33b/{0},{1},{2}?units=si".format(lat, lon, epoch_time)
    response = requests.get(dark_sky_URL)
    weather_api_data = response.json()
    return weather_api_data
#**************************************************************************************
def epoch_time():
    return int(datetime.datetime.now().timestamp())
#**************************************************************************************
def epoch_time_to_human(value):
    result  = ''   + datetime.datetime.fromtimestamp(value).strftime('%A')[:3]
    result += ', ' + datetime.datetime.fromtimestamp(value).strftime('%d')
    result += ' '  + datetime.datetime.fromtimestamp(value).strftime('%B')
    result += ' '  + datetime.datetime.fromtimestamp(value).strftime('%Y')
    return result
#**************************************************************************************
def epoch_time_day_name(value):
    day_name = datetime.datetime.fromtimestamp(value).strftime('%A')[:3]
    return day_name
#**************************************************************************************
def get_location():
    headers = {'Accept': 'application/json'}
    # KEY = '3f55b07b200471d3ee97ce323483420208527f68fb6d3f0e57df3db5'
    # resp = requests.get('https://api.ipdata.co?api-key={}'.format(KEY), headers=headers)
    # response_body = resp.json()
    # latitude = response_body['latitude']
    latitude = 46.9480
    # longitude = response_body['longitude']
    longitude = 7.4474
    # city = response_body['city']
    city = 'bern'
    return latitude, longitude, city
#**************************************************************************************
# def currentTime(par):
#       current_time = epoch_time()+(86400*par)
#       return current_time

CITY = ''
def index(request): 
    # TIME
    current_time = epoch_time()
    current_time_human = epoch_time_to_human(current_time)
    # CURRENT TEMPERATURE  °C MORE PRECISE
    current_temp_inC = round(weather_api(get_location()[0], get_location()[1], epoch_time())["currently"]["temperature"])
    # CURRENT SUMMARY (SHORT)
    current_summary = weather_api(get_location()[0], get_location()[1], epoch_time())["currently"]["summary"]
    # CURRENT WIND SPEED Meters per second.
    current_wind_speed_mps = weather_api(get_location()[0], get_location()[1], epoch_time())["currently"]["windSpeed"]
    current_wind_speed_kph = round(current_wind_speed_mps * 3.6)
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

    icon1 = weather_api(get_location()[0], get_location()[1], epoch_time()+(86400*1))["currently"]["icon"]
    if '-' in icon1:
      icon1 = ''.join(icon1.split('-')[:-1])
    else:
      icon1
    icon2 = weather_api(get_location()[0], get_location()[1], epoch_time()+(86400*2))["currently"]["icon"]
    if '-' in icon2:
      icon2 = ''.join(icon2.split('-')[:-1])
    else:
      icon2  
    icon3 = weather_api(get_location()[0], get_location()[1], epoch_time()+(86400*3))["currently"]["icon"]
    if '-' in icon3:
      icon3 = ''.join(icon3.split('-')[:-1])
    else:
      icon3  
    icon4 = weather_api(get_location()[0], get_location()[1], epoch_time()+(86400*4))["currently"]["icon"]
    if '-' in icon4:
      icon4 = ''.join(icon4.split('-')[:-1])
    else:
      icon4  
    icon5 = weather_api(get_location()[0], get_location()[1], epoch_time()+(86400*5))["currently"]["icon"]
    if '-' in icon5:
      icon5 = ''.join(icon5.split('-')[:-1])
    else:
      icon5  
    icon6 = weather_api(get_location()[0], get_location()[1], epoch_time()+(86400*6))["currently"]["icon"]
    if '-' in icon6:
      icon6 = ''.join(icon6.split('-')[:-1])
    else:
      icon6  

    weather = {
      'time': current_time_human,
      'city': get_location()[2],
      'icon': icon,
      'wind_kph': current_wind_speed_kph,
      'summary_short': current_summary,
      'summary_extended': summary,
      'temp_high_C': temp_high_inC,
      'temp_low_C': temp_low_inC,

      'temp_C' : round(weather_api(get_location()[0], get_location()[1], epoch_time())["currently"]["temperature"]),
      'temp_C1': round(weather_api(get_location()[0], get_location()[1], epoch_time()+(86400*1))["currently"]["temperature"]),
      'temp_C2': round(weather_api(get_location()[0], get_location()[1], epoch_time()+(86400*2))["currently"]["temperature"]),
      'temp_C3': round(weather_api(get_location()[0], get_location()[1], epoch_time()+(86400*3))["currently"]["temperature"]),
      'temp_C4': round(weather_api(get_location()[0], get_location()[1], epoch_time()+(86400*4))["currently"]["temperature"]),
      'temp_C5': round(weather_api(get_location()[0], get_location()[1], epoch_time()+(86400*5))["currently"]["temperature"]),
      'temp_C6': round(weather_api(get_location()[0], get_location()[1], epoch_time()+(86400*6))["currently"]["temperature"]),

      'icon' : icon,
      'icon1': icon1,
      'icon2': icon2,
      'icon3': icon3,
      'icon4': icon4,
      'icon5': icon5,
      'icon6': icon6,

      'days_name' : epoch_time_day_name(epoch_time()),
      'days_name1': epoch_time_day_name(epoch_time()+(86400*1)),
      'days_name2': epoch_time_day_name(epoch_time()+(86400*2)),
      'days_name3': epoch_time_day_name(epoch_time()+(86400*3)),
      'days_name4': epoch_time_day_name(epoch_time()+(86400*4)),
      'days_name5': epoch_time_day_name(epoch_time()+(86400*5)),
      'days_name6': epoch_time_day_name(epoch_time()+(86400*6)),
      # 'weekdays': ls,
    }
#**************************************************************************************  
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CityForm(request.POST)
        if form.is_valid():
            global CITY
            city_entered = list(form.cleaned_data.values())[0]
            CITY = str(city_entered)
    # if a GET (or any other method) we'll create a blank form
    else:
        form = CityForm()

    context = {'weather' : weather, 'form': form}

    return render(request, 'Date/index.html', context, CITY)#returns the index.html template
# _____________________________________________________________________________________________



def indexTwo(request):
    cityname = index(request)._headers['content-type'][1]
    # TIME
    current_time = epoch_time()
    current_time_human = epoch_time_to_human(current_time)
    # CURRENT TEMPERATURE  °C MORE PRECISE
    current_temp_inC = round(weather_api(fun(cityname)[0], fun(cityname)[1], epoch_time())["currently"]["temperature"])
    # CURRENT SUMMARY (SHORT)
    current_summary = weather_api(fun(cityname)[0], fun(cityname)[1], epoch_time())["currently"]["summary"]
    # CURRENT WIND SPEED Meters per second.
    current_wind_speed_mps = weather_api(fun(cityname)[0], fun(cityname)[1], epoch_time())["currently"]["windSpeed"]
    current_wind_speed_kph = round(current_wind_speed_mps * 3.6)
    # SUMMARY EXTENDED
    summary = weather_api(fun(cityname)[0], fun(cityname)[1], epoch_time())["daily"]["data"][0]["summary"]
    # DAILY HIGH TEMPERATURE AND LOW TEMPERATURE °C
    temp_high_inC = round(weather_api(fun(cityname)[0], fun(cityname)[1], epoch_time())["daily"]["data"][0]["temperatureHigh"])
    temp_low_inC = round(weather_api(fun(cityname)[0], fun(cityname)[1], epoch_time())["daily"]["data"][0]["temperatureLow"])
    # ICON OF THE CURRENT TEMP
    icon = weather_api(fun(cityname)[0], fun(cityname)[1], epoch_time())["currently"]["icon"]
    if '-' in icon:
      icon = ''.join(icon.split('-')[:-1])
    else:
      icon 
    icon1 = weather_api(fun(cityname)[0], fun(cityname)[1], epoch_time()+(86400*1))["currently"]["icon"]
    if '-' in icon1:
      icon1 = ''.join(icon1.split('-')[:-1])
    else:
      icon1
    icon2 = weather_api(fun(cityname)[0], fun(cityname)[1], epoch_time()+(86400*2))["currently"]["icon"]
    if '-' in icon2:
      icon2 = ''.join(icon2.split('-')[:-1])
    else:
      icon2  
    icon3 = weather_api(fun(cityname)[0], fun(cityname)[1], epoch_time()+(86400*3))["currently"]["icon"]
    if '-' in icon3:
      icon3 = ''.join(icon3.split('-')[:-1])
    else:
      icon3  
    icon4 = weather_api(fun(cityname)[0], fun(cityname)[1], epoch_time()+(86400*4))["currently"]["icon"]
    if '-' in icon4:
      icon4 = ''.join(icon4.split('-')[:-1])
    else:
      icon4  
    icon5 = weather_api(fun(cityname)[0], fun(cityname)[1], epoch_time()+(86400*5))["currently"]["icon"]
    if '-' in icon5:
      icon5 = ''.join(icon5.split('-')[:-1])
    else:
      icon5  
    icon6 = weather_api(fun(cityname)[0], fun(cityname)[1], epoch_time()+(86400*6))["currently"]["icon"]
    if '-' in icon6:
      icon6 = ''.join(icon6.split('-')[:-1])
    else:
      icon6  

    city_weather = {
      'time': current_time_human,
      'city': cityname,
      'icon': icon,
      'wind_kph': current_wind_speed_kph,
      'summary_short': current_summary,
      'summary_extended': summary,
      'temp_high_C': temp_high_inC,
      'temp_low_C': temp_low_inC,

      'temp_C' : round(weather_api(fun(cityname)[0], fun(cityname)[1], epoch_time())["currently"]["temperature"]),
      'temp_C1': round(weather_api(fun(cityname)[0], fun(cityname)[1], epoch_time()+(86400*1))["currently"]["temperature"]),
      'temp_C2': round(weather_api(fun(cityname)[0], fun(cityname)[1], epoch_time()+(86400*2))["currently"]["temperature"]),
      'temp_C3': round(weather_api(fun(cityname)[0], fun(cityname)[1], epoch_time()+(86400*3))["currently"]["temperature"]),
      'temp_C4': round(weather_api(fun(cityname)[0], fun(cityname)[1], epoch_time()+(86400*4))["currently"]["temperature"]),
      'temp_C5': round(weather_api(fun(cityname)[0], fun(cityname)[1], epoch_time()+(86400*5))["currently"]["temperature"]),
      'temp_C6': round(weather_api(fun(cityname)[0], fun(cityname)[1], epoch_time()+(86400*6))["currently"]["temperature"]),

      'icon' : icon,
      'icon1': icon1,
      'icon2': icon2,
      'icon3': icon3,
      'icon4': icon4,
      'icon5': icon5,
      'icon6': icon6,

      'days_name' : epoch_time_day_name(epoch_time()),
      'days_name1': epoch_time_day_name(epoch_time()+(86400*1)),
      'days_name2': epoch_time_day_name(epoch_time()+(86400*2)),
      'days_name3': epoch_time_day_name(epoch_time()+(86400*3)),
      'days_name4': epoch_time_day_name(epoch_time()+(86400*4)),
      'days_name5': epoch_time_day_name(epoch_time()+(86400*5)),
      'days_name6': epoch_time_day_name(epoch_time()+(86400*6)),
      # 'weekdays': ls,
    }
    
    #**************************************************************************************  
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CityForm(request.POST)
        if form.is_valid():
            global CITY
            city_entered = list(form.cleaned_data.values())[0]
            CITY = str(city_entered)
    # if a GET (or any other method) we'll create a blank form
    else:
        form = CityForm()

    city_context = {'city_weather' : city_weather, 'form': form}


    return render(request, 'Date/index.1.html', city_context)#returns the index.html template








 

# def indexTwo(request):
#     print(index(request))
#     return HttpResponse('This is indexTwo')

#     #**************************************************************************************
#     # if this is a POST request we need to process the form data
#     if request.method == 'POST':
#         # create a form instance and populate it with data from the request:
#         form = CityForm(request.POST)
#         if form.is_valid():
#             city_entered = list(form.cleaned_data.values())[0]
#             # CITY = fun(city_entered)
#             print(city_entered)
#     # if a GET (or any other method) we'll create a blank form
#     else:
#         form = CityForm()
#     #**************************************************************************************
#     return render(request, 'Date/index.html', {'form': form})

