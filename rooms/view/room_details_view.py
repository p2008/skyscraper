from django.contrib import messages
from django.shortcuts import render, redirect
from rooms.models import Room, Reservation


# As a user, I want to see room details with name, capacity and projector availability.
def room_details(request, rid):
    try:
        room = Room.objects.get(pk=rid)
        title = f'room {room.name}'
        reservation_raw = Reservation.objects.filter(room_id=rid)
        reservation_dates = [date.date for date in reservation_raw]

        return render(request, 'room_details_view.html',
                      {'title':title,
                       'room': room,
                       'reservation_dates': reservation_dates})
    except Exception as e:
        print(e)
        messages.error(request, 'Nie znaleziono sali')
        return redirect('all_rooms')
