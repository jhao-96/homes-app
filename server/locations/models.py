from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    photo = models.CharField(max_length=200)
    availableUnits = models.IntegerField()
    wifi = models.BooleanField(default=True)
    laundry = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name