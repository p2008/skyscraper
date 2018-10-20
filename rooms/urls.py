from django.contrib import admin
from django.urls import path
from .view import all_rooms_view


urlpatterns = [
    path('', all_rooms_view.all_rooms, name='all_rooms'),

]