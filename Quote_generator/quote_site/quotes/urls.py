from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.random_quotes, name='home'),
    path('submit/', views.submit_quote, name='submit_quote')
]
