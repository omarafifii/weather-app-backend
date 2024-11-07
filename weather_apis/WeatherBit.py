from .BaseWeatherAPI import BaseWeatherAPI
from requests import request
import os

class WeatherBit(BaseWeatherAPI):
    def __init__(self, *args, **kwargs):
        self.base_url = 'https://api.weatherbit.io/v2.0'
        self.key = os.getenv('WEATHER_BIT_KEY')

    def get_current_weather(self, city):
        params = {
            'city': city,
            'key': self.key,
        }

        url = self.base_url + '/current'

        response = request("GET", url=url, params=params)
        return response.json()

    def get_previous_weather(self, city, start_date, end_date):
        params = {
            'city': city,
            'key': self.key,
            'start_date': start_date,
            'end_date': end_date,
        }

        url = self.base_url + '/history/hourly'

        response = request("GET", url=url, params=params)
        return response.json()