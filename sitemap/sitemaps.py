from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse



class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'
    def items(self):
        return ['index','about','shop','contact']
    def location(self, item):
        return reverse(item)