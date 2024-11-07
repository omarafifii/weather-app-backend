from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Copay weather app!</p>"

@app.route("/v1/weather/<city>")
def get_weather(city):
    pass

if __name__ == '__main__':
    app.run()