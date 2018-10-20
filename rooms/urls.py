from django.urls import path
from .view import all_rooms_view, room_remove_view, room_details_view

urlpatterns = [
    # Paweł
    path('', all_rooms_view.all_rooms, name='all_rooms'),

    # Mateusz
    # place your code here

    # Kewin
    # place your code here

    # Artem
    path('remove/<int:rid>/', room_remove_view.room_remove, name='room_remove'),
    path('details/<int:rid>/', room_details_view.room_details, name='room_detail'),
]