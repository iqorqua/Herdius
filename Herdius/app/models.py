from django.db import models
from django.contrib.auth.models import AbstractUser

class MyUser(AbstractUser):
    country=models.CharField(max_length=30, blank=False)
    address=models.TextField(max_length=500, blank=False)
    postal_code=models.CharField(max_length=30, blank=False)
    phone=models.CharField(max_length=30, blank=False)
    bday = models.DateField(null=False, blank=False)
    picture_id = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg', blank = True)
    avatar = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg', blank = True)


class Test():
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)