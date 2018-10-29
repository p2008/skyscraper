from django import forms
from django.forms import ModelForm
from .models import Room, Reservation


class EditRoomForm(ModelForm):
    class Meta:
        model = Room
        fields = ['name', 'capacity', 'is_projector']
        widgets = {
            'name': forms.TextInput(
                attrs={'placeholder': 'room name',
                       'class': ''}),
            'capacity': forms.NumberInput(
                attrs={'class': 'number'}),
            'is_projector': forms.CheckboxInput(
                attrs={'class': ''})
        }


class RoomReservationForm(ModelForm):
    class Meta:
        model = Reservation
        fields = ['date', 'comment', 'room']
        widgets = {
            'date': forms.SelectDateWidget,
            'comment': forms.Textarea(attrs={'cols': 30, 'rows': 3})
        }
