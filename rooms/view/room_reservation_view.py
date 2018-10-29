from datetime import datetime, timedelta
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View
from ..forms import RoomReservationForm


class RoomReservationView(View):
    template_name = 'room_reservation_view.html'
    form_class = RoomReservationForm

    def get(self, request):
        tomorrow = datetime.now() + timedelta(1)
        form = self.form_class(initial={
            'room': request.GET.get('rid'),
            'date': tomorrow.strftime('%Y-%m-%d')})
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Booked')
            return redirect('room_details', rid=request.GET.get('rid'))

        messages.error(request, 'Error occurred, please try again')
        return render(request, self.template_name, {'form': form})
