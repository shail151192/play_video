# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('thumbnail', models.CharField(max_length=255)),
                ('video', models.CharField(max_length=255)),
                ('uploaded_on', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
