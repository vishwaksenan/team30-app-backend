from django.shortcuts import render
from rest_framework import viewsets
from .serializers import HostSerializer, GuestSerializer, HostAvailabilitySerialzer, BookingSerializer
from .models import Host, Guest, HostAvailability, Booking

class HostView(viewsets.ModelViewSet):
  serializer_class = HostSerializer
  queryset = Host.objects.all()

class GuestView(viewsets.ModelViewSet):
  serializer_class = GuestSerializer
  queryset = Guest.objects.all()

class HostAvailabilityView(viewsets.ModelViewSet):
  serializer_class = HostAvailabilitySerialzer
  queryset = HostAvailability.objects.all()

class BookingView(viewsets.ModelViewSet):
  serializer_class = BookingSerializer
  queryset = Booking.objects.all()