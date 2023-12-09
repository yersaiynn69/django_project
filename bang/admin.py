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

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'time_create', 'message')
    search_fields = ('name',)

class PayAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone_number', 'time_create')
    search_fields = ('time_create',)

admin.site.register(Pay,PayAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(AboutMe,AboutMeAdmin)
admin.site.register(Feedback,FeedbackAdmin)


