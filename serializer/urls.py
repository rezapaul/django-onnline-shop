from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView , TokenRefreshView




urlpatterns = [
    path('',views.products ,name='products_json') ,
    path('<int:product_id>',views.product , name='product_json') ,
    path('search',views.search ,name='products_search_json') ,
    path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh', TokenRefreshView.as_view(), name='token_refresh'),
]