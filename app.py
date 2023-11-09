from flask import Flask, render_template
import requests
from dotenv import load_dotenv, dotenv_values

config = dotenv_values('.env')

app = Flask(__name__)

def get_weather_data(city):
    API_KEY=config['API_KEY']
    url = f' https://api.openweathermap.org/data/2.5/weather?q={ city }&units=metric&lang=es&appid={API_KEY}'
    r = requests.get(url).json()
    print(r)
    return r


@app.route('/city')
def city():
    get_weather_data(city)
    return get_weather_data(city)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/clima')
def clima():
    return 'Obten toda la informacion del clima'


if __name__=='__main__':
    app.run(debug=True)

    

