from django.shortcuts import render
import urllib.request
import json

# Create your views here.

# def weather(request):
    
#     return render(request, 'weather.html')


def weather(request):
    if request.method == 'POST':
        city = request.POST['city']
        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&unit=metric&appid=b628a7d2c27f2ee337e0c0cfe94f6277').read()
        json_data = json.loads(source)
        data = {
            "country_code": str(json_data['sys']['country']),
            "coordinate": str(json_data['coord']['lon'])+ ', ' + str(json_data['coord']['lat']),
            "temp": str(json_data['main']['temp']),
            "pressure": str(json_data['main']['pressure']),
            "humidity": str(json_data['main']['humidity']),
            "main": str(json_data['weather'][0]['main']),
            "description": str(json_data['weather'][0]['description']),
            'icon': json_data['weather'][0]['icon'],
        }
        print(data)
    else:
        data= {}
    
    return render(request, "weather.html", data)
