from weather_apis import WeatherBit, WeatherAPI

class Logic_Handler:
    
    def __init__(self):
        self.weather_api = WeatherAPI()
        self.weather_bit = WeatherBit()

    def calculate_weather_data(self, city):
        self.weather_api.get_current_weather(city)

    def calculate_current_data(self, city):
        pass

    def calculate_previous_data(self, city):
        pass

    def combine_api_data(self, city):
        pass

    def get_forecast_from_previous_data(self, city):
        pass