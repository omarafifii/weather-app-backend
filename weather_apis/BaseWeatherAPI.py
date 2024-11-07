from abc import ABC

class BaseWeatherAPI(ABC):
    def __init__(self, *args, **kwargs):
        pass

    def get_current_weather(self, city):
        pass

    def get_previous_weather(self, city):
        pass