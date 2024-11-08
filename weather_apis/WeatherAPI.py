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

    def extract_current_data(self, weather_data):
        return {
            'temp': weather_data['current']['temp_c'],
            'humidity': weather_data['current']['humidity'],
            'wind_speed': weather_data['current']['wind_kph'],
        }

    def extract_previous_data(self, weather_data, time_now):
         time_now = int(time_now)
         return {
            'past_hour': {
                'temp': weather_data['forecast']['forecastday'][1]['hour'][-1]['temp_c'],
                'humidity': weather_data['forecast']['forecastday'][1]['hour'][-1]['humidity'],
                'wind_speed': weather_data['forecast']['forecastday'][1]['hour'][-1]['wind_kph'],
            },
            'yesterday_prev': {
                'temp': weather_data['forecast']['forecastday'][0]['hour'][time_now-1]['temp_c'],
                'humidity': weather_data['forecast']['forecastday'][0]['hour'][time_now-1]['humidity'],
                'wind_speed': weather_data['forecast']['forecastday'][0]['hour'][time_now-1]['wind_kph'],
            },
            'yesterday_curr': {
                'temp': weather_data['forecast']['forecastday'][1]['hour'][time_now]['temp_c'],
                'humidity': weather_data['forecast']['forecastday'][1]['hour'][time_now]['humidity'],
                'wind_speed': weather_data['forecast']['forecastday'][1]['hour'][time_now]['wind_kph'],
            }
        }