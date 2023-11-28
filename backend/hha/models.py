import datetime

from django.core.exceptions import ValidationError
from django.db import models

class Host(models.Model):
  first_name = models.CharField(max_length=150)

class Guest(models.Model):
  first_name = models.CharField(max_length=150)

class HostAvailability(models.Model):
  host = models.ForeignKey(Host, on_delete=models.CASCADE)
  date = models.DateField(default=datetime.date.today)

  class Meta:
    verbose_name_plural = 'Host Availabilities'
    unique_together = ('host', 'date')

class Booking(models.Model):
  host = models.ForeignKey(Host, on_delete=models.CASCADE)
  guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
  date = models.DateField(default=datetime.date.today)

  class Meta:
     unique_together = (('host', 'guest', 'date'), ('guest', 'date'))

  def save(self, *args, **kwargs):
        availability = HostAvailability.objects.filter(host=self.host, date=self.date)
        if availability.exists():
            availability.delete()
            super().save(*args, **kwargs)
        else:
            raise ValidationError('No availability found for the given host and date.')