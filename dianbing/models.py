from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User


class Sakesman(models.Model):
    user = models.OneToOneField(User)
    parent_id = models.IntegerField(default=0)
    phone = models.IntegerField(default=0)
