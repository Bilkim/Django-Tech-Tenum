from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE

# Create your models here
class Users(AbstractUser):
    is_subscriber = models.BooleanField(default=False)
    is_publisher = models.BooleanField(default=False)
    email = models.EmailField('Email Address', unique=True)
    phone = models.CharField('Phone Number', max_length=150, unique = True, null=True)

    
    
class Subscriber(models.Model):
    user = models.OneToOneField(Users, on_delete=models.CASCADE, primary_key=True)
    
class PublisherData(models.Model):
    data = models.TextField(blank=True)  
