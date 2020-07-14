from django.urls import path
from . import views
from .feeds import LatestProductFeed


urlpatterns = [
    path('',views.shop,name='shop'),
    path('product/<int:product_id>', views.product , name='product'),
    path('addcomment', views.addcomment , name='addcomment'),
    path('addtocart', views.AddToCart , name='addtocart'),
    path('search', views.search , name='search'),
    path('category', views.category, name='category'),
    path('rss' , LatestProductFeed() ,name='feed') ,
]