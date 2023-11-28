from django.shortcuts import get_list_or_404
from rest_framework import viewsets
from urllib import response
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

class HostAvailabilityByDateView(viewsets.ViewSet):
  def list(self, request, date=None):
    queryset = get_list_or_404(HostAvailability, date=date)
    serializer = HostAvailabilitySerialzer(queryset, many=True)
    return response(serializer.data)



class BookingView(viewsets.ModelViewSet):
  serializer_class = BookingSerializer
  queryset = Booking.objects.all()