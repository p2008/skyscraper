from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=64)
    capacity = models.PositiveIntegerField()
    is_projector = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Reservation(models.Model):
    date = models.DateField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE,
                             related_name='reservation')
    comment = models.TextField(blank=True)  # blank=True added to enable empty
                                            # comments while booking
