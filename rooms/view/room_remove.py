from django.http.response import HttpResponse
from django.shortcuts import render
from rooms.models import Room
from django.contrib import messages

# As a user, I want to remove room on click remove.

def room_remove(request, rid):
    Room.objects.get(pk=rid)
    messages.success(request, 'Usunięto salę')
    return render(request, 'room_remove_view.html')
