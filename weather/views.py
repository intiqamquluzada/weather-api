from django.shortcuts import render
import requests


def index(request):
    url = 'http://api.openweathermap.org/data/2.5/forecast'
    params = {
        'lat': 40.407660,
        'lon': 49.847768,
        'appid': 'XXXXX'
    }

    response = requests.get(url, params=params)

    context = {
        # 'api_data': response.json(),
        "city": response.json()['city'],
        "weather": response.json()['list'][1]['main']
    }

    return render(request, 'index.html', context)
