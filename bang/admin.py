from django.contrib import admin
from .models import *

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'photo', 'is_published')
    list_display_links = ('id','title')
    search_fields = ('title', 'price')
    list_editable = ('is_published', )
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {"slug": ("title",)}

class AboutMeAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'photo', 'content')
    search_fields = ('title',)


admin.site.register(Product,ProductAdmin)
admin.site.register(AboutMe,AboutMeAdmin)

