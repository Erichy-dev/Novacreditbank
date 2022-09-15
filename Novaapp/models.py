from django.db import models

# Create your models here.

class Data(models.Model):
    name = models.CharField(max_length=100)
    body = models.CharField(max_length=1000000)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)  
    other_name = models.CharField(max_length=200)
    email = models.EmailField()
    profile_image = models.ImageField(blank=True)
    city = models.CharField(max_length= 100)
    title = models.TextField(null=True, blank=True)
    middlename = models.TextField(null=True, blank=True)
    adreess = models.TextField(null=True, blank=True)
    country = models.TextField(null=True, blank=True)
    state = models.TextField(blank=True, verbose_name="Biography (Age, Language, Location...)")
    pin = models.IntegerField()
    available = models.TextField(null=True, blank=True)
    checkings = models.TextField(null=True, blank=True)
    savings = models.TextField(null=True, blank=True)
    phone_number = models.TextField(null=True, blank=True)
    first_his = models.TextField(null=True, blank=True)
    second_history =  models.TextField(null=True, blank=True)
    third_history = models.TextField(null=True, blank=True)
    last_history = models.TextField(null=True, blank=True)
    newstate = models.TextField(null=True, blank=True)




