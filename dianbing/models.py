from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User


class Sakesman(models.Model):
    user = models.OneToOneField(User)
    parent_id = models.IntegerField(default=0)
    phone = models.IntegerField(default=0)


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=128)
    image = models.CharField(max_length=128, default="")
    video = models.CharField(max_length=128, default="")
    price = models.IntegerField(default=0)
    stock = models.IntegerField(default=0)
    is_delete = models.SmallIntegerField(default=0)
    create_time = models.DateTimeField(auto_now_add=True)

    def base_info(self):
        return dict(product_id=self.product_id,
                    product_name=self.product_name,
                    image=self.image,
                    video=self.video,
                    price=self.price,
                    stock=self.stock,
                    create_time=self.create_time)
