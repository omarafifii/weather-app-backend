from weather_apis.WeatherAPI import WeatherAPI
from weather_apis.WeatherBit import WeatherBit
from datetime import datetime, timedelta

class Logic_Handler:
    
    def __init__(self):
        self.weather_api = WeatherAPI()
        self.weather_bit = WeatherBit()

    def calculate_weather_data(self, city):
        yesterday_date = (datetime.today() - timedelta(days=1)).strftime('%Y-%m-%d')
        today_date = (datetime.today()).strftime('%Y-%m-%d')
        time_now = datetime.now().strftime('%H')

        weatherbit_current = self.weather_bit.get_current_weather(city)
        weatherapi_current = self.weather_api.get_current_weather(city)

        weatherbit_history = self.weather_bit.get_previous_weather(city, yesterday_date, today_date)
        weatherapi_history = self.weather_api.get_previous_weather(city, yesterday_date, today_date)

        weatherbit_current_clean = self.weather_bit.extract_current_data(weatherbit_current)
        weatherapi_current_clean = self.weather_api.extract_current_data(weatherapi_current)

        weatherbit_history_clean = self.weather_bit.extract_previous_data(weatherbit_history, time_now)
        weatherapi_history_clean = self.weather_api.extract_previous_data(weatherapi_history, time_now)

        current_combined = self.combine_current_data(weatherapi_current_clean, weatherbit_current_clean)

        history_combined = self.combine_previous_data(weatherapi_history_clean, weatherbit_history_clean)

        forcast = self.get_forecast_from_previous_data(current_combined, history_combined)

        return {
            'current': current_combined,
            # 'history': history_combined,
            'forecast': forcast,
        }

    def combine_current_data(self, api1, api2):
        result = self.combine_data_from_2_dicts(api1, api2)
        return result

    def combine_previous_data(self, api1, api2):
        result = {}

        for key in api1:
            result[key] = self.combine_data_from_2_dicts(api1[key], api2[key])

        return result

    def combine_data_from_2_dicts(self, dict1, dict2):
        result = {}
        for key in dict1:
            percent_change = abs((dict1[key] - dict2[key]) / dict1[key]) * 100
            result[key] = dict1[key] * 0.6 + dict2[key] * 0.4 if percent_change < 15 else dict1[key]
        
        return result

    def get_forecast_from_previous_data(self, current_data, history_data):
        result = {}

        for key in current_data:
            # calculate recent change
            recent = current_data[key] - history_data['past_hour'][key]
            
            # calculate historical change
            historical = history_data['yesterday_curr'][key] - history_data['yesterday_prev'][key]

            weighted_average = recent * 0.6 + historical * 0.4
            result[key] = weighted_average + current_data[key]
            if key == 'humidity' and result[key] > 100:
                result[key] = 95

        return result