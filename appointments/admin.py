from django.contrib import admin
from .models import *

class AppointmentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'photo', 'is_published', 'organisation', 'service_type', 'status' )
    list_display_links = ('id','title')
    search_fields = ('title', 'content')
    list_editable = ('is_published', )
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Appointments,AppointmentsAdmin)
