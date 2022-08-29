from django.contrib import admin
from django.urls import path
from .views import contactform, home


urlpatterns = [
    path('contact',contactform, name="contact")
]