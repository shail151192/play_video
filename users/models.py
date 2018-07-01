from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Authuser(User):
    class Meta:
        proxy = True

    @classmethod
    def save(cls, data):
        obj={}
        obj['first_name'] = data['first_name']
        obj['last_name'] = data['last_name']
        obj['email'] = data['email']
        obj['password'] = data['password']
        obj['username'] = data['username']

        user = User.objects.create_user(**obj)
        return user