from .BaseWeatherAPI import BaseWeatherAPI
from requests import request
import os

class WeatherAPI(BaseWeatherAPI):
    def __init__(self, *args, **kwargs):
        self.base_url = 'http://api.weatherapi.com/v1/'
        self.key = os.getenv('WEATHER_API_KEY')

    def get_current_weather(self, city):
        params = {
            'q': city,
            'key': self.key,
        }

        url = self.base_url + '/current.json'

        response = request("GET", url=url, params=params)
        return response.json()

    def get_previous_weather(self, city, start_date, end_date):
        params = {
            'q': city,
            'key': self.key,
            'dt': start_date,
            'end_dt': end_date,
        }

        url = self.base_url + '/history.json'

        response = request("GET", url=url, params=params)
        return response.json()