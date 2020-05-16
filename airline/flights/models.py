from django.db import models

# Create your models here.
class Airport(models.Model):
    code=models.CharField(max_length=3,blank = True)
    city=models.CharField(max_length=64,blank = True)

    def __str__(self):
        return f"{self.code} ({self.code})"


class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="depatures")
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration= models.IntegerField()

    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination}"

