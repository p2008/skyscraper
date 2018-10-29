from django.contrib import messages
from django.shortcuts import render
from django.views import View

from rooms.models import Room


class AllRooms(View):
    template_name = 'all_rooms_view.html'

    def get(self, request):
        rooms = Room.objects.order_by('pk')

        return render(request, self.template_name,
                      {'rooms': rooms})

