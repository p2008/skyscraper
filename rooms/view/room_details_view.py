from django.contrib import messages
from django.shortcuts import render, redirect
from rooms.models import Room


# No. 6: As a user, I want to see room details when click on name room.
def room_details(request, rid):
    try:
        room = Room.objects.get(pk=rid)
        title = f'room {room.name}'
        return render(request, 'room_details_view.html', {'title':title, 'room': room})
    except:
        messages.error(request, 'Nie znaleziono sali')
        return redirect('all_rooms')

