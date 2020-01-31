from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=300)

class Type(models.Model):
    name= models.CharField(max_length=200)

class Event(models.Model):
    person = models.ForeignKey(User, on_delete=models.CASCADE, related_name="User")
    name = models.CharField(max_length=200)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    place= models.CharField(max_length=200)
    address= models.CharField(max_length=200)
    creation_date=models.DateTimeField(default=timezone.now)
    start_date=models.DateTimeField()
    finish_date=models.DateTimeField()
    type=models.ForeignKey(Type, on_delete=models.CASCADE)