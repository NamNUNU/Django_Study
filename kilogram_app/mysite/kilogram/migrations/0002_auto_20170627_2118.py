# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-27 12:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kilogram', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='thumbnail',
            field=models.ImageField(blank=True, upload_to=b''),
        ),
    ]
