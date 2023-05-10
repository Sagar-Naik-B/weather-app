from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from .settings import WEATHER_API

class WeatherAPIView(APIView):
    def post(self, request, format=None):
        city = request.POST.get('city')

        if not city:
            return Response({'error': 'city parameter is missing.'}, status=400)
        
        # Retrieve weather data from OpenWeatherMap API 
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API}'
        response = requests.get(url)
        if response.status_code == 404:
            return Response({'error': 'City not found.'}, status=404)
        elif response.status_code != 200:
            return Response({'error': 'An error occurred while fetching weather data.'}, status=500)

        weather_data = response.json()
        return Response(weather_data)
