from abc import ABC

class BaseWeatherAPI(ABC):
    def __init__(self, *args, **kwargs):
        pass

    def get_current_weather(self, city):
        pass

    def get_previous_weather(self, city, start_date, end_date):
        pass

    def extract_current_data(self, weather_data):
        pass

    def extract_previous_data(self, weather_data, time_now):
         pass