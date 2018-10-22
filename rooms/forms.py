from django.forms import ModelForm
from .models import Room


class EditRoomForm(ModelForm):
    class Meta:
        model = Room
        fields = ['name', 'capacity', 'is_projector']

