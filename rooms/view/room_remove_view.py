from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect
from rooms.models import Room
from django.contrib import messages


def room_remove(request, rid):
    try:
        room = Room.objects.get(pk=rid)
        room.delete()
        messages.success(request, f'{room.name} has been removed')
    except ObjectDoesNotExist:
        messages.error(request, 'There is no such room')
    return redirect('all_rooms')
