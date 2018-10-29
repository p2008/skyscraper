from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views import View
from ..forms import EditRoomForm
from ..models import Room
from django.contrib import messages


class AddRoom(View):
    form_class = EditRoomForm
    template_name = 'edit_room_view.html'

    def get(self, request):
        form = self.form_class()

        return render(request, self.template_name, {'form': form})

    def post(self, request):
        room = Room()
        form = self.form_class(request.POST, instance=room)

        if form.is_valid():
            form.save()
            messages.success(request, f'{room.name} room added successfully')
            return redirect(reverse('all_rooms'))

        messages.error(request, "An error occurred. Your form hadn't been save")
        return render(request, self.template_name, {'form': form})

