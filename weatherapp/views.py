from django.shortcuts import render
import requests
import json
import datetime


def weather(request):  
    print(request.POST)

    if 'city' in request.POST and request.POST['city'] != '':
        city = request.POST['city']
    else:
        city = 'Seoul'
    appid = 'b628a7d2c27f2ee337e0c0cfe94f6277'
    URL = 'http://api.openweathermap.org/data/2.5/weather'
    PARAMS = {'q':city, 'appid':appid, 'units':'metric'}
    r = requests.get(url=URL, params=PARAMS)
    res = r.json()
    data = {
        "country_code": str(res['sys']['country']),
        'city': city,
        "coordinate": str(res['coord']['lon'])+ ', ' + str(res['coord']['lat']),
        "temp": str(res['main']['temp']),
        "pressure": str(res['main']['pressure']),
        "humidity": str(res['main']['humidity']),
        "main": str(res['weather'][0]['main']),
        "description": str(res['weather'][0]['description']),
        'time': datetime.date.today(),
        'icon': res['weather'][0]['icon'],
    }
    print(data)
    return render(request, "weather.html", data)
