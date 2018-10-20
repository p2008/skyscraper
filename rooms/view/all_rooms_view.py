from django.shortcuts import render

from rooms.models import Room


def all_rooms(request):
    rooms = Room.objects.all()
    return render(request, 'all_rooms_view.html', {'rooms': rooms})
