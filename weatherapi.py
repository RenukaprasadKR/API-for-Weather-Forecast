from flask import Flask, jsonify, request
import requests
from datetime import datetime

app = Flask(__name__)
api_key = "5e2b250925b6337db4d077da5a6f4ee5" #API key

def kelvin_to_celsius(kelvin_temp):
    return kelvin_temp - 273.15

def format_date(timestamp):
    return datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d')

@app.route('/weather', methods=['GET'])
def get_weather():
    locations = request.args.getlist('location')  # Accept multiple locations as a list

    if not locations:
        return jsonify({'error': 'At least one location is required'}), 400

    weather_data = []
    for location in locations:
        city, state = map(str.strip, location.split(','))
        data = get_weather_data(city, state)
        weather_data.append(data)

    return jsonify(weather_data)

def get_weather_data(city, state):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': f'{city},{state}',
        'appid': api_key,
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()

        # Extract relevant information from the API response
        weather_info = {
            'city': data['name'],
            'date': format_date(data['dt']),
            'day': datetime.utcfromtimestamp(data['dt']).strftime('%A'),
            'temperature': kelvin_to_celsius(data['main']['temp']),
            'max_temperature': kelvin_to_celsius(data['main']['temp_max']),
            'min_temperature': kelvin_to_celsius(data['main']['temp_min']),
            'description': data['weather'][0]['description'],
            'precipitation': data['weather'][0].get('main', 'N/A'),
            'humidity': data['main'].get('humidity', 'N/A'),
            'wind_speed': data['wind'].get('speed', 'N/A'),
        }

        return weather_info

    except requests.exceptions.RequestException as e:
        return {'error': f'Error fetching data from OpenWeatherMap: {str(e)}'}

if __name__ == '__main__':
    app.run(debug=True)
