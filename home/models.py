from __future__ import unicode_literals

from django.db import models


class Video(models.Model):
    name = models.CharField(max_length=255)
    thumbnail = models.FileField(upload_to='images/', max_length=255, null=True)
    video = models.FileField(upload_to='videos/', null=True, verbose_name='')
    uploaded_by = models.CharField(max_length=255)
    uploaded_on = models.DateTimeField(auto_now=True)
