from flask import Flask
from logic import Logic_Handler
import traceback

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Copay weather app!</p>"

@app.route("/v1/weather/<city>")
def get_weather(city):
    logic_handler = Logic_Handler()
    try:
        data = logic_handler.calculate_weather_data(city)
        return data
    except Exception as e:
        print(Exception, e)
        print(traceback.format_exc())
        return {'message': 'An error occured'}, 400

if __name__ == '__main__':
    app.run()