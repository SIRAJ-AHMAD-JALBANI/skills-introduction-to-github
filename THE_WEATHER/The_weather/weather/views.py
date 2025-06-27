# The_weather_app/weather/views.py
import requests
from django.shortcuts import render

def index(request):
    # --- Configuration ---
    # Replace 'YOUR_WEATHERAPI_COM_API_KEY' with your actual API key from WeatherAPI.com
    api_key = '587c4cf59a7347a589835928252006' # <--- UPDATE THIS WITH YOUR WEATHERAPI.COM KEY!
    city = 'Dera Ghazi Khan' # Example: 'Lahore', 'Karachi', 'Islamabad'

    # WeatherAPI.com API endpoint for current weather
    # 'aqi=no' is added to avoid pulling air quality data if not needed, making response slightly smaller
    url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no'

    city_weather = {} # Initialize an empty dictionary for weather data

    try:
        response = requests.get(url).json()

        # WeatherAPI.com's error handling is usually based on a 'error' key
        if 'error' not in response:
            city_weather = {
                'city': response['location']['name'],
                'temperature': response['current']['temp_c'], # Temperature in Celsius
                'description': response['current']['condition']['text'],
                'icon': response['current']['condition']['icon'], # This is a full URL to the icon
            }
        else:
            # Handle WeatherAPI.com specific errors
            city_weather = {
                'city': city,
                'temperature': 'N/A',
                'description': f"Error: {response['error']['message']}",
                'icon': 'https://cdn.weatherapi.com/v4/assets/api/weather/64x64/day/113.png', # Default icon URL for error
            }

    except requests.exceptions.RequestException as e:
        city_weather = {
            'city': city,
            'temperature': 'N/A',
            'description': f"Network Error: {e}. Check your internet connection.",
            'icon': 'https://cdn.weatherapi.com/v4/assets/api/weather/64x64/day/113.png',
        }
    except KeyError:
        city_weather = {
            'city': city,
            'temperature': 'N/A',
            'description': 'Error: Unexpected data format from weather API.',
            'icon': 'https://cdn.weatherapi.com/v4/assets/api/weather/64x64/day/113.png',
        }

    context = {'city_weather': city_weather}
    return render(request, 'weather/index.html', context)
