from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect
from rooms.models import Reservation
from django.contrib import messages


def reservation_cancel(request, res_id, rid):
    try:
        reservation = Reservation.objects.get(pk=res_id)
        reservation.delete()
        messages.success(request, f'Reservation for {reservation.date} has been canceled')
    except ObjectDoesNotExist:
        messages.error(request, 'There is no such reservation')
    return redirect('room_details', rid=rid)
