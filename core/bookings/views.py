from django.shortcuts import render

# Create your views here.
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Booking

@csrf_exempt
def create_booking(request):
    if request.method == "POST":
        data = json.loads(request.body)

        booking = Booking.objects.create(
            name=data.get("name"),
            phone=data.get("phone"),
            location=data.get("location"),
            event_date=data.get("date"),
            package=data.get("package"),
            services=data.get("services"),
            payment=data.get("payment"),
        )

        return JsonResponse({
            "status": "success",
            "message": "Booking saved successfully",
            "booking_id": booking.id
        })

from django.shortcuts import render

def home(request):
    return render(request, "index.html")
