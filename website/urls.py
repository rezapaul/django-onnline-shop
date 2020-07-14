from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static 
from django.views.generic import TemplateView



urlpatterns = [
    
    path('', include('pages.urls')),
    path('', include('order.urls')),
    path('', include('coupon.urls')),
    path('', include('sitemap.urls')),
    path('admin/', admin.site.urls),
    path('shop/', include('products.urls')),
    path('accounts/', include('accounts.urls')),
    path('api/v1/', include('serializer.urls')),
    path('adminorders/', include('adminorders.urls')),
    path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type='text/plain')),

]+ static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)
