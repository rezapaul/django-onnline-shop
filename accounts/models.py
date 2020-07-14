from django.db import models





class Billing(models.Model):
    user_id = models.IntegerField()
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    street_address = models.CharField(max_length=200)
    apartment_address = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200)
    email = models.CharField(max_length=300)
    phone = models.CharField(max_length=200)
    order_notes = models.TextField(blank=True)


    def __str__(self):
        return self.street_address




class Favorite(models.Model):
    user_id = models.IntegerField() 
    product_id = models.IntegerField()
    product_name = models.CharField(max_length=200)
    product_photo = models.CharField(max_length=300)
    product_price = models.CharField(max_length=200)
    




class Curency(models.Model):
    user_username = models.CharField(max_length=200,blank=True)
    curency = models.IntegerField(default=0)
    etebar = models.CharField(max_length=200,default=curency,blank=True)

    def __str__(self):
        return self.etebar
