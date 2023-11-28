from rest_framework import serializers

from .models import Host, Guest, HostAvailability, Booking

class HostSerializer(serializers.ModelSerializer):

  class Meta:
    model = Host
    fields = ('id', 'first_name')

class GuestSerializer(serializers.ModelSerializer):

  class Meta:
    model = Guest
    fields = ('id', 'first_name')

class HostAvailabilitySerialzer(serializers.ModelSerializer):

  class Meta:
    model = HostAvailability
    fields = ('id', 'host', 'date')
    depth = 1

class BookingSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Booking
    fields = ('id', 'host', 'guest', 'date')
    depth = 1