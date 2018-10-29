from django.urls import path
from .view import (all_rooms_view,
                   room_remove_view,
                   edit_room_view,
                   room_details_view,
                   room_reservation_view)

urlpatterns = [
    # Paweł
    path('', all_rooms_view.all_rooms, name='all_rooms'),
    path('edit_room/', edit_room_view.EditRoom.as_view(),
         name='edit_room'),

    # Mateusz
    # place your code here

    # Kewin
    path('reservation/', room_reservation_view.RoomReservationView.as_view(),
         name='room_reservation'),

    # Artem
    path('remove/<int:rid>/', room_remove_view.room_remove, name='room_remove'),
    path('details/<int:rid>/', room_details_view.room_details, name='room_details'),
]
