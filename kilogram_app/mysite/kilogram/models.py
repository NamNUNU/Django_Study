# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings

# Create your models here.

def user_path(instance, filename):
    from random import choice
    import string
    arr = [choice(string.ascii_letters) for _ in range(8) ]
    pid = ''.join(arr)
    extention = filename.split('.')[-1]
    return '%s/%s.%s' % (instance.owner.username, pid, extention)

class Photo(models.Model):
    image = models.ImageField(upload_to=user_path)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    thumbnail = models.ImageField(blank = True)
    comment = models.CharField(max_length=255)
    pub_date = models.DateTimeField(auto_now_add=True)