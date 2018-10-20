from django.shortcuts import render
from .models import Room

# Create your views here.


def all_rooms(request):
    rooms = Room.objects.all()
    return render(request, 'all_rooms_view.html', {'rooms': rooms})
