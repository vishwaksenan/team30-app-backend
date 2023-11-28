import datetime

from django.db import models

class Host(models.Model):
  first_name = models.CharField(max_length=150)

class Guest(models.Model):
  first_name = models.CharField(max_length=150)

class HostAvailability(models.Model):
  host = models.OneToOneField(Host, on_delete=models.CASCADE)
  date = models.DateField(default=datetime.date.today)

  class Meta:
    verbose_name_plural = "Host Availabilities"

class Booking(models.Model):
  host = models.OneToOneField(Host, on_delete=models.CASCADE)
  guest = models.OneToOneField(Guest, on_delete=models.CASCADE)
  date = models.DateField(default=datetime.date.today)

  