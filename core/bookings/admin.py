from django.contrib import admin
from bookings.models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "phone",
        "location",
        "event_date",
        "package",
        "payment",
        "created_at",
    )
