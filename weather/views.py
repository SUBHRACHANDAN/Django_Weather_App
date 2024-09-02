import requests
from django.shortcuts import render
from django.conf import settings

def weather_view(request):
    weather_data = None
    if 'city' in request.GET:
        city = request.GET['city']
        api_key = settings.OPENWEATHERMAP_API_KEY
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        if response.status_code == 200:
            weather_data = response.json()
    
    return render(request, 'weather/weather.html', {'weather_data': weather_data})
