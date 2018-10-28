from django import forms
from django.forms import ModelForm
from .models import Room, Reservation


class EditRoomForm(ModelForm):
    class Meta:
        model = Room
        fields = ['name', 'capacity', 'is_projector']


class RoomReservationForm(ModelForm):
    class Meta:
        model = Reservation
        fields = ['date', 'comment']
        widgets = {
            'date': forms.SelectDateWidget,
            'comment': forms.TextArea(attrs={'cols': 10, 'rows': 2})
        }