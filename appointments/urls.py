from django.urls import path

from appointments.views import *

urlpatterns = [
    path('service/',  ServiceView.as_view(), name='service'),
    path('service/<slug:appointment_slug>/,',  AppointmentDetailView.as_view(), name='show_appointment'),
]
