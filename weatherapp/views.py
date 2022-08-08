from django.shortcuts import render, redirect
import requests
import datetime
from timezonefinder import TimezoneFinder
import pytz
from .models import City
from .forms import CityForm

def get_tz(a, b):
    tz = TimezoneFinder()
    tz = tz.timezone_at(lng=a, lat=b)
    return tz

def get_localtime(tz):
    tz=pytz.timezone(tz)
    localtime = datetime.datetime.now(tz)
    str_localtime = localtime.strftime('%Y-%m-%d %H:%M:%S')
    return str_localtime    


def weather(request):  
    
    appid = 'b628a7d2c27f2ee337e0c0cfe94f6277'
    URL = 'http://api.openweathermap.org/data/2.5/weather'
    weather_data = []
    err_msg = ""
    message = ""
    message_class = ""

    
    if request.method == 'POST':
        # print(request.POST)
        form = CityForm(request.POST)

        
        if form.is_valid():
            new_city = form.cleaned_data['name']
            existing_city_count = City.objects.filter(name=new_city).count()
            
            if existing_city_count == 0:
                PARAMS = {'q':new_city, 'appid':appid, 'units':'metric'}
                r = requests.get(url=URL, params=PARAMS).json()
                if r['cod'] == 200:
                    form.save()
                else:
                    err_msg = "City does not exist"
            else:
                err_msg = "City already exists in the database"
        # print(err_msg)

        if err_msg:
            message = err_msg
            message_class = 'btn btn-outline-danger'
        else:
            message = "City added successfully"
            message_class = 'btn btn-outline-success'

            
    form = CityForm()
    cities = City.objects.all()

    
    for city in cities:
        PARAMS = {'q':city, 'appid':appid, 'units':'metric'}

        r = requests.get(url=URL, params=PARAMS).json()
        print(r)
        tz = get_tz(r['coord']['lon'], r['coord']['lat'])
        localtime = get_localtime(tz)
        
        
        city_weather = {
            'city': city.name,
            'temp': r['main']['temp'],
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon'],
            'main': r['weather'][0]['main'],
            'localtime': localtime
        }
        
        weather_data.append(city_weather)
    # print(weather_data)
    context = {'weather_data': weather_data, 
               'form': form,
               'message': message,
               'message_class': message_class,
               }
    return render(request, 'weather.html', context)
        

def delete_city(request, city_name):
    City.objects.get(name = city_name).delete()
    return redirect('/weather/')