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

    def extract_current_data(self, weather_data):
        # convert windspeed from m/s to km/h
        wind_speed = weather_data['data'][0]['wind_spd']
        adjusted_wind_speed = wind_speed * 3.6
        return {
            'temp': weather_data['data'][0]['temp'],
            'humidity': weather_data['data'][0]['rh'],
            'wind_speed': adjusted_wind_speed,
        }

    def extract_previous_data(self, weather_data, time_now):
         return {
            'past_hour': {
                'temp': weather_data['data'][-1]['temp'],
                'humidity': weather_data['data'][-1]['rh'],
                'wind_speed': weather_data['data'][-1]['wind_spd']*3.6,
            },
            'yesterday_prev': {
                'temp': weather_data['data'][-23]['temp'],
                'humidity': weather_data['data'][-23]['rh'],
                'wind_speed': weather_data['data'][-23]['wind_spd']*3.6,
            },
            'yesterday_curr': {
                'temp': weather_data['data'][-24]['temp'],
                'humidity': weather_data['data'][-24]['rh'],
                'wind_speed': weather_data['data'][-24]['wind_spd']*3.6,
            }
        }