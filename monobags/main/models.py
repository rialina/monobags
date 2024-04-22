from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    photo = models.ImageField(upload_to='', max_length=100)
    users = models.ManyToManyField(User, blank=True)
