# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from enum import IntEnum
from django.contrib.auth.models import User


class OrderStatus(IntEnum):
    NORMAL = 1
    EXCEPT = 2


class PaymentType(IntEnum):
    COD = 1
    ONLINE = 2


class Sakesman(models.Model):
    user = models.OneToOneField(User)
    parent_id = models.IntegerField(default=0)
    phone = models.IntegerField(default=0)


class ProductType(models.Model):
    type_id = models.AutoField(primary_key=True)            # 产品ID
    type_name = models.CharField(max_length=64)
    type_desc = models.CharField(max_length=128)
    status = models.SmallIntegerField(default=1)            # 0：不可用，1：可用
    pos = models.IntegerField(default=1)                    # 位置
    create_time = models.DateTimeField(auto_now_add=True)

    def base_info(self):
        return dict(type_id=self.type_id,
                    type_name=self.type_name,
                    type_desc=self.type_desc)


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)                     # 产品ID
    product_type = models.ForeignKey(ProductType)                       # 产品类型
    product_name = models.CharField(max_length=128)                     # 产品名称
    images = models.CharField(max_length=512, default="")               # 图片
    price = models.IntegerField(default=0)                              # 单价
    stock = models.IntegerField(default=0)                              # 库存
    status = models.SmallIntegerField(default=1)          # 0:删除，1:正常
    operator = models.CharField(max_length=64)                          # 操作人
    update_time = models.DateTimeField(auto_now=True)                   # 更新时间
    create_time = models.DateTimeField(auto_now_add=True)               # 创建时间

    def base_info(self):
        return dict(product_id=self.product_id,
                    product_name=self.product_name,
                    product_type=self.product_type,
                    images=self.images,
                    price=self.price,
                    stock=self.stock,
                    create_time=self.create_time)


class ProductModel(models.Model):
    model_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product)
    model_name = models.CharField(max_length=128)
    model_param = models.CharField(max_length=512)                     # 产品型号
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
                    product_model=self.product_model,
                    create_time=self.create_time)


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product)
    product_model = models.CharField(max_length=512)
    name = models.CharField(max_length=128)
    phone = models.CharField(max_length=128, default="")
    province = models.CharField(max_length=128, default="")
    city = models.CharField(max_length=128, default="")
    area = models.CharField(max_length=128, default="")
    detail_address = models.CharField(max_length=256, default="")
    payment_type = models.SmallIntegerField(default=0)
    operator = models.CharField(max_length=128, default="")
    remarks = models.TextField(default="")
    status = models.SmallIntegerField(default=0)
    create_time = models.DateTimeField(auto_now_add=True)

    def base_info(self):
        return dict(order_id=self.order_id,
                    name=self.name,
                    phone=self.phone,
                    address="{} {} {}".format(self.province, self.city, self.detail_address),
                    payment_type=self.payment_type,
                    operator=self.operator,
                    status=self.status,
                    create_time=self.create_time)
