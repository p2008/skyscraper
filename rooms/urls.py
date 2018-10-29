from django.urls import path
from .view import (all_rooms_view,
                   room_remove_view,
                   edit_room_view,
                   add_new_room_view,
                   room_details_view,
                   room_reservation_view,
                   room_search_view,
                   reservation_cancel_view)

urlpatterns = [
    path('', all_rooms_view.AllRooms.as_view(), name='all_rooms'),

    path('edit_room/', edit_room_view.EditRoom.as_view(), name='edit_room'),
    path('add_room/', add_new_room_view.AddRoom.as_view(), name='add_room'),
    path('details/<int:rid>/', room_details_view.room_details, name='room_details'),
    path('remove/<int:rid>/', room_remove_view.room_remove, name='room_remove'),

    path('search/', room_search_view.room_search, name='search_room'),


    path('reservation/', room_reservation_view.RoomReservationView.as_view(),
         name='room_reservation'),
    path('reservation-cancel/<int:res_id>/<int:rid>/', reservation_cancel_view.reservation_cancel,
         name='reservation_cancel'),
]


