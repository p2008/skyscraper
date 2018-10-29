from datetime import datetime
from django.contrib import messages
from django.shortcuts import render, redirect
from rooms.models import Room, Reservation


def room_details(request, rid):
    try:
        room = Room.objects.get(pk=rid)
        title = f'room {room.name}'
        today = datetime.now().strftime('%Y-%m-%d')
        reservation_raw = Reservation.objects.filter(room_id=rid).filter(date__gte=today)
        reservation_dates = [date.date for date in reservation_raw]

        return render(request, 'room_details_view.html',
                      {'title': title,
                       'room': room,
                       'reservation_dates': reservation_dates})
    except Exception as e:
        print(e)
        messages.error(request, 'Nie znaleziono sali')
        return redirect('all_rooms')
