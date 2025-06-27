# The_weather_app/weather/urls.py
from django.urls import path
from . import views # Import views from the current app

app_name = 'weather' # Namespace for this app's URLs

urlpatterns = [
    path('', views.index, name='index'), # Maps the root URL of this app to the 'index' view
]