from flask import Flask, render_template, request
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
API_KEY = os.getenv("WEATHER_API_KEY")

def get_weather_data(city_name):
    try:
        url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city_name}&aqi=no"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        return {
            'temperature': data['current']['temp_c'],
            'condition': data['current']['condition']['text'].lower(),
            'icon': "https:" + data['current']['condition']['icon'],
            'humidity': data['current']['humidity'],
            'wind': data['current']['wind_kph'],
            'feels_like': data['current']['feelslike_c'],
            'pressure': data['current']['pressure_mb'],
            'country': data['location']['country']
        }

    except Exception as e:
        return {'error': f"❌ Could not fetch weather: {str(e)}"}

@app.route('/', methods=['GET', 'POST'])
def index():
    city = ""
    weather_data = None
    error = None

    if request.method == "POST":
        city = request.form.get("city", "").strip()
        if city:
            weather_data = get_weather_data(city)
            if "error" in weather_data:
                error = weather_data["error"]
                weather_data = None
        else:
            error = "Please enter a valid city name"

    return render_template("index.html", city=city, weather_data=weather_data, error=error)

if __name__ == "__main__":
    app.run(debug=True)
