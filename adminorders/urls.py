from django.urls import path
from . import views


urlpatterns = [
    path('',views.allorders,name='allorders'),
    path('detail/<int:bought_id>',views.orderdetail,name='orderdetail'),
]