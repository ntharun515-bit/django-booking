from django.urls import path
from core.bookings.views import create_booking


urlpatterns = [
    path("create/", create_booking),
]
