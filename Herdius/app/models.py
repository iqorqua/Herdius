from django.db import models
from django.contrib.auth.models import AbstractUser
from app.django_encrypt_file import EncryptionService, ValidationError
from django.core.files import File 
import time
import os
import threading
from django.conf import settings
#from django_encrypted_filefield.fields import (
#    EncryptedFileField,
#    EncryptedImageField
#)

class MyUser(AbstractUser): 
    country=models.CharField(max_length=30, blank=False)
    address=models.TextField(max_length=500, blank=False)
    postal_code=models.CharField(max_length=30, blank=False)
    phone=models.CharField(max_length=30, blank=False)
    bday = models.DateField(null=False, blank=False)
    avatar = models.ImageField(upload_to = 'avatars/', default = 'pic_folder/no-img.jpg', blank = False)
    encrypted_data = models.CharField(max_length=300, blank=False)

    @property
    def image_id(self):
            service = EncryptionService(raise_exception=False)
            try:
                n = str(self.encrypted_data).split('/')[-1]
                file = File(open(self.encrypted_data, 'rb'), name=n)
                password = self.password #getattr(settings, "ENCRYPTION_KEY", None)
                decrypt_file = service.decrypt_file(file, password)
                my_thread = threading.Thread(target=kamikadze, args=(decrypt_file.file.name,))
                my_thread.start()
            except ValidationError as e:
               print(e)
            return decrypt_file.name


def kamikadze(filename):
    time.sleep(5)
    os.remove(filename)
