from django.urls import path
from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticViewSitemap
sitemaps = {
    'static': StaticViewSitemap
}


urlpatterns = [
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),
]