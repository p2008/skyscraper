from django.shortcuts import render

from forms import RoomReservationForm


class RoomReservationView(ModelView):
    template_name = 'room_reservation_view'
    form = RoomReservationForm

    def get(self, request):

        return render(request, self.template_name, {'form': self.form})