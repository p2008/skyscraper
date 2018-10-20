from django.urls import path
from .view import all_rooms_view, room_remove
# import all_rooms_view
# import room_remove

urlpatterns = [
    path('', all_rooms_view.all_rooms, name='all_rooms'),


    # Artem
    path('remove/<int:rid>/', room_remove.room_remove, name='room_remove'),

]