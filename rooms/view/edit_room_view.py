from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views import View
from ..forms import EditRoomForm
from ..models import Room
from django.contrib import messages


class EditRoom(View):
    form_class = EditRoomForm
    template_name = 'edit_room_view.html'

    def get(self, request):
        room_id = request.GET.get('pk')
        room = get_object_or_404(Room, pk=room_id)
        form = self.form_class(initial={'name': room.name,
                                        'capacity': room.capacity,
                                        'is_projector': room.is_projector})

        return render(request, self.template_name, {'form': form})

    def post(self, request):
        room_id = request.GET.get('pk')
        room = get_object_or_404(Room, pk=room_id)
        form = self.form_class(request.POST, instance=room)

        if form.is_valid():
            form.save()
            messages.success(request, f'{room.name} room edited successfully')
            return redirect(reverse('all_rooms'))

        messages.error(request, "An error occurred. Your form hadn't been save")
        return render(request, self.template_name, {'form': form})

