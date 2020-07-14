from django.urls import path
from . import views



urlpatterns = [
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('register',views.register,name='register'),
    path('addtofavorite',views.addtofavorite,name='addtofavorite'),
    path('removefavorite',views.removefavorite,name='removefavorite'),
    path('favorites',views.favorite_inf,name='favorites'),
    path('details/<int:buy_id>',views.details,name='details'),
    path('wallet',views.wallet,name='wallet'),
]