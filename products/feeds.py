from django.contrib.syndication.views import Feed
from django.urls import reverse
from .models import Product

class LatestProductFeed(Feed):
   title = "Products From My Shop"
   link = "/shop/feeds"
   description = "Updates on changes and additions to posts published in the starter."

   def items(self):
       return Product.objects.order_by('-product_date')

   def item_name(self, item):
       return item.name
   
   def item_date(self, item):
       return item.product_date

   def item_description(self, item):
       return item.description[:200]

   def item_link(self, item):
       return reverse('product', args=[item.pk])