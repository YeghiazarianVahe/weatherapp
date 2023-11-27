from django.shortcuts import render
import requests
from weather.models import City
from weather.forms import CityForm


def index(req):
    api_key = '3fc7f4f2f199349c339576874c0184a2'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + api_key

    if req.method == 'POST':
        form = CityForm(req.POST)
        form.save()

    form = CityForm()
    cities = City.objects.all()
    all_cities = []

    for city in cities:
        res = requests.get(url.format(city.name)).json()
        city_info = {
            'city': city.name,
            'temp': res['main']['temp'],
            'icon': res['weather'][0]['icon']
        }
        all_cities.append(city_info)

    context = {
        'all_info': all_cities,
        'form': form
    }

    return render(req, 'weather/index.html', context)
