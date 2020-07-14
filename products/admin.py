from django.contrib import admin
from .models import Product,Product_comments


class AdminProduct(admin.ModelAdmin):
    list_display = ('id' ,'name','quality', 'price' ,'availibility' ,'is_published'  ,'category')
    list_display_links = ('id' ,'name')
    list_per_page = 25 
    search_fields = ('name', 'price' ,'category','description','size','width','height','depth','weight')

admin.site.register(Product,AdminProduct)




class AdminComment(admin.ModelAdmin):
    list_display = ('id' ,'fullname','is_published','product_id')
    list_display_links = ('id' ,'fullname')
    list_per_page = 25 
    search_fields = ('fullname', 'content')

admin.site.register(Product_comments ,AdminComment)    
