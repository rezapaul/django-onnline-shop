from django.contrib import admin
from .models import Contact


class AdminContact(admin.ModelAdmin):
    list_display = ('id' ,'subject','first_name', 'last_name')
    list_display_links = ('id' ,'subject')
    list_per_page = 25 
    search_fields = ('subject', 'first_name' ,'last_name','content')


admin.site.register(Contact,AdminContact)
