from django.db import models
from datetime import datetime




class Cart_Added(models.Model):
    user_id = models.IntegerField()
    product_id = models.IntegerField()
    product_name = models.CharField(max_length=300)
    product_price = models.DecimalField(max_digits=20,decimal_places=1)
    product_quantity = models.IntegerField(default=1)
    product_total = models.DecimalField(max_digits=20,decimal_places=1)
    product_size = models.CharField(max_length=200,blank=True)
    product_photo = models.ImageField(upload_to='cart/products/%Y/%m/%d/')
    addtocart_date = models.DateTimeField(default=datetime.now ,blank=True)
    is_active = models.BooleanField(default=True)
    is_ordering = models.BooleanField(default=False)
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return self.product_name



class Order_done(models.Model):
    buy_id = models.IntegerField()
    user_id = models.IntegerField()
    product_id = models.IntegerField()
    product_name = models.CharField(max_length=300)
    product_price = models.DecimalField(max_digits=20,decimal_places=1)
    product_quantity = models.IntegerField(default=1)
    product_total = models.DecimalField(max_digits=20,decimal_places=1)
    product_size = models.CharField(max_length=200,blank=True)
    
    def __str__(self):
        return self.buy_id



class User_orders(models.Model):
    buy_id = models.IntegerField()
    user_id = models.IntegerField()

    def __str__(self):
        return self.buy_id