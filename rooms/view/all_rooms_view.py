from django.contrib import messages
from django.shortcuts import render
from django.views import View

from rooms.models import Room


class AllRooms(View):
    template_name = 'all_rooms_view.html'

    def get(self, request):
        name = request.GET.get('name')
        min_capacity = request.GET.get('min_capacity')
        day = request.GET.get('day')
        projector = request.GET.get('projector')
        no_filter = True

        search_form = {
            'name': name,
            'min_capacity': min_capacity,
            'day': day,
            'projector': projector,
            'no_filter': no_filter,
        }

        rooms = Room.objects

        if name:
            no_filter = False
            rooms = Room.objects.filter(name__icontains=name).order_by('pk')

        if min_capacity:
            no_filter = False
            rooms = rooms.filter(capacity__gte=min_capacity).order_by('pk')

        if day:
            no_filter = False
            rooms = rooms.exclude(reservation__date=day).order_by('pk')

        if projector:
            no_filter = False
            rooms = rooms.filter(is_projector=True).order_by('pk')

        if no_filter:
            rooms = rooms.order_by('pk')

        if not rooms:
            messages.error(request, 'No free rooms for given criteria')

        return render(request, self.template_name,
                      {'rooms': rooms, 'search_form': search_form})
