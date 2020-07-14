from django.urls import path
from . import views



urlpatterns = [
    path('cart',views.cart,name='cart'),
    path('checkout',views.checkout,name='checkout'),
    path('confermation',views.confermation,name='confermation'),
    path('deletefromcart',views.deletefromcart,name='deletefromcart'),
    path('deleteallcart',views.deleteallcart,name='deleteallcart'),
    path('placeorder',views.placeorder,name='placeorder'),
]