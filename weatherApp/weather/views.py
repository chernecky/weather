from django.shortcuts import render
import requests
from .models import City

def index(request):
    appid = '813fceb17db4f854e1035e85bea7a51c'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid
    cities = City.objects.all()

    all_cities = []
    for city in cities:
        response = requests.get(url.format(city.name))
        city_info = {
        'city': city.name,
        'temp': response["main"][0]["temp"],
        'icon': response["weather"][0]["icon"]
    }
    context = {'all_info': all_cities}
    return render(request, 'weather/index.html', context)
