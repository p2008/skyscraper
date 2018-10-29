from django.shortcuts import render

from rooms.models import Room
from django.views import View


class AllRooms(View):
    template_name = 'all_rooms_view.html'

    def get(self, request):
        rooms = Room.objects.order_by('pk')

        return render(request, self.template_name, {'rooms': rooms})

    def post(self, request):
        search_string = request.POST.get('search')
        rooms = Room.objects.filter(name__icontains=search_string).order_by('pk')

        return render(request, self.template_name, {'rooms': rooms})
