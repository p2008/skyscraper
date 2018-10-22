from django.urls import path
from .view import all_rooms_view, room_remove, edit_room_view

# import all_rooms_view, room_remove, edit_room_view

urlpatterns = [
    path('', all_rooms_view.all_rooms, name='all_rooms'),
    path('edit_room/', edit_room_view.EditRoom.as_view(),
         name='edit_room'),

    # Artem
    path('remove/<int:rid>/', room_remove.room_remove, name='room_remove'),

]
