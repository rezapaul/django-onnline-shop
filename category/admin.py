from django.contrib import admin
from .models import Category


class AdminCategory(admin.ModelAdmin):
    list_display = ('id' ,'name')
    list_display_links = ('id' ,'name')
    list_per_page = 25 
    search_fields = ('name', 'description')
admin.site.register(Category,AdminCategory)
