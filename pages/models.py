from django.db import models




class Contact(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    subject = models.CharField(max_length=200,blank=True)
    content = models.TextField()

    def __str__(self):
        return self.subject
