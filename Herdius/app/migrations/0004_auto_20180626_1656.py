# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-26 13:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_myuser_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='image',
            field=models.ImageField(default='', upload_to=''),
        ),
    ]
