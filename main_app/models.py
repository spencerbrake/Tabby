from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import CharField, TextField

# Create your models here.

class Trip(models.Model):
    title = models.CharField(max_length=100)
    from_location = models.CharField(max_length=100)
    to_location = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
class Photo(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    image = CharField(max_length=200)

class Diary_Entry(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    content = models.TextField()

class Notes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    content = TextField()
