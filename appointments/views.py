from django.shortcuts import render, get_object_or_404
from django.views import View
from django.http import HttpResponse

from appointments.models import Appointments

class ServiceView(View):
    template_name = 'service.html'

    def get(self, request, *args, **kwargs):
        # Get all appointments from the database
        appointments = Appointments.objects.all()

        # Creating a context to pass to the template
        context = {
            'appointments': appointments,
            'title': 'Service',
        }

        # Return an HTTP response with the rendered template and context
        return render(request, self.template_name, context=context)

class AppointmentDetailView(View):
    template_name = 'appointments.html'

    def get(self, request, appointment_slug, *args, **kwargs):
        # Get an article by its unique identifier (slug)
        appointment = get_object_or_404(Appointments, slug=appointment_slug)

        # Creating a context to pass to the template
        context = {
            'appointment': appointment,
            'title': appointment.title,
        }

        # Return an HTTP response with the rendered template and context
        return render(request, self.template_name, context=context)
