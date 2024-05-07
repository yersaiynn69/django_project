from django.contrib import admin
from .models import *

class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'photo', 'content')
    search_fields = ('title',)

admin.site.register(AboutUs,AboutUsAdmin)

