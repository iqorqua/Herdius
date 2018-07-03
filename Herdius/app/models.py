from django.db import models
from django.contrib.auth.models import AbstractUser

class MyUser(AbstractUser):
    country=models.CharField(max_length=30, blank=True),
    address=models.TextField(max_length=500, blank=True)
    postal_code=models.CharField(max_length=30, blank=True),
    phone=models.CharField(max_length=30, blank=True),
    bday = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg', blank = True)

class Test():
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)