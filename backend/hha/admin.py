from django.contrib import admin

from .models import Host, Guest, HostAvailability, Booking

class HostAdmin(admin.ModelAdmin):
  list_display = ("first_name",)

class GuestAdmin(admin.ModelAdmin):
  list_display = ("first_name",)

class HostAvailibilityAdmin(admin.ModelAdmin):
  list_display = ("host","date")

class BookingAdmin(admin.ModelAdmin):
  list_display = ("host", "guest", "date")

admin.site.register(Host, HostAdmin)
admin.site.register(Guest, GuestAdmin)
admin.site.register(HostAvailability, HostAvailibilityAdmin)
admin.site.register(Booking, BookingAdmin)