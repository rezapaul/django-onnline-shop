from django.db import models
from category.models import Category
from datetime import datetime



class Product(models.Model):

    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=20,decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    availibility = models.BooleanField(default=True)
    description = models.TextField()
    size1 = models.CharField(max_length=200,default='Small')
    size2 = models.CharField(max_length=200,blank=True)
    size3 = models.CharField(max_length=200,blank=True)
    size4 = models.CharField(max_length=200,blank=True)
    size5 = models.CharField(max_length=200,blank=True)
    color = models.CharField(max_length=200)
    width = models.CharField(max_length=200)
    height = models.CharField(max_length=200)
    depth = models.CharField(max_length=200)
    weight = models.CharField(max_length=200)
    quality = models.CharField(max_length=200,default='Yes',blank=True)
    product_date = models.DateTimeField(default=datetime.now ,blank=True)
    is_published = models.BooleanField(default=False)
    photo_1 = models.ImageField(upload_to='products/%Y/%m/%d/')
    photo_2 = models.ImageField(upload_to='products/%Y/%m/%d/',blank=True)
    photo_3 = models.ImageField(upload_to='products/%Y/%m/%d/',blank=True)

    def __str__(self):
        return self.name

    


class Product_comments(models.Model):

    product_id =  models.IntegerField()
    fullname = models.CharField(max_length=300)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    content = models.TextField()
    is_published = models.BooleanField(default=False)
    comment_date = models.DateTimeField(default=datetime.now ,blank=True)

    def __str__(self):
        return self.fullname

