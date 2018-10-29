from datetime import datetime
from django.contrib import messages
from django.shortcuts import render, redirect
from rooms.models import Room, Reservation


def room_details(request, rid):
    try:
        room = Room.objects.get(pk=rid)
        title = f'room {room.name}'
        current_day = datetime.now().strftime('%Y-%m-%d')
        reservations_raw = Reservation.objects.filter(room_id=rid).filter(date__gte=current_day)
        reservations = [reservation for reservation in reservations_raw]

        return render(request, 'room_details_view.html',
                      {'title': title,
                       'room': room,
                       'reservations': reservations})
    except Exception as e:
        print(e)
        messages.error(request, 'There is no such room')
        return redirect('all_rooms')
