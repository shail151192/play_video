# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-06-27 12:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video',
            field=models.FileField(null=True, upload_to='/media', verbose_name=''),
        ),
    ]