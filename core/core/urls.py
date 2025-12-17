from django.contrib import admin
from django.urls import path, include
from bookings.views import home

urlpatterns = [
    path('', home),  # 👈 HOME PAGE
    path('admin/', admin.site.urls),
    path('api/bookings/', include('bookings.urls')),
]
