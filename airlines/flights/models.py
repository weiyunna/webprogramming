from django.db import models

# Create your models here.
class Airport (models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)


class Flight (models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="depatures")
    destination=  models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()

class Passenger (models.Model):
    first= models.CharField(max_length=64)
    last= models.CharField(max_length=64)
    flights= models.ManyToManyField(Flight, blank=True, related_name="passengers")
