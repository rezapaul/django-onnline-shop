from django.db import models




class Coupon(models.Model):
    name = models.CharField(max_length=200)
    currency = models.IntegerField()
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name


class Used_coupon(models.Model):
    user_id = models.IntegerField()
    name = models.CharField(max_length=200)