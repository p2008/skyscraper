from django.http.response import HttpResponse


def room_reservation(request, rid):

    return HttpResponse(rid)