# -*- coding: utf-8 -*-
import json
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from dianbing.models import (
    Order,
    Product,
    ProductModel,
    OrderStatus,
    PaymentType,
)
from utils.timetool import TimeHandler
from utils.snowflake import Snowflake
from django.core.paginator import (
    Paginator,
    PageNotAnInteger,
    EmptyPage)
from _base import BaseApi


__author__ = 'Sunlf'


@login_required
def order_list(request):
    page = request.GET.get("index", 1)
    size = request.GET.get("size", 20)
    spec = dict()
    order_id = request.GET.get("order_id")
    if order_id:
        spec["order_id"] = order_id
    product_name = request.GET.get("product_name")
    if product_name:
        spec["product_name__icontains"] = product_name
    name = request.GET.get("name")
    if name:
        spec["name__icontains"] = name
    phone = request.GET.get("phone")
    if phone:
        spec["phone"] = phone
    status = request.GET.get("status")
    if status:
        spec["status"] = status

    objects = Order.objects.filter(**spec).order_by("-create_time")
    paginator = Paginator(objects, size)
    try:
        records = paginator.page(page)
    except PageNotAnInteger:
        records = paginator.page(1)
    except EmptyPage:
        records = paginator.page(paginator.num_pages)
    data = []
    for record in records:
        data.append(record.base_info())
    return JsonResponse(dict(data=data, total=paginator.count))


def order_create(request):
    args = json.loads(request.body)
    try:
        product_id = args.get("product_id")
        if product_id:
            product = Product.objects.get(pk=int(product_id))
            if product:
                obj = Order()
                snowflake = Snowflake()
                _id = snowflake.generate()
                obj.order_id = _id
                obj.product = product
                obj.name = args.get("name", "")
                obj.phone = args.get("phone", "")
                obj.province = args.get("province", "")
                obj.city = args.get("city", "")
                obj.area = args.get("area", "")
                obj.detail_address = args.get("detail_address", "")
                obj.payment_type = PaymentType.COD
                obj.status = OrderStatus.NORMAL
                obj.save()
            else:
                return JsonResponse(dict(code=-1, message="cannot find product for {}".format(product_id)))
        else:
            return JsonResponse(dict(code=-1, message="cannot find argument product_id"))
    except ObjectDoesNotExist:
        return JsonResponse(dict(code=-1, message="cannot find product for {}".format(product_id)))
    return JsonResponse(dict(code=1, message="success"))


@login_required
def order_update(request):
    args = json.loads(request.body)
    obj = Order.objects.get(pk=args["product_id"])
    for key in args:
        setattr(obj, key, args[key])
    obj.save()
    return JsonResponse(dict(data=obj.base_info()))


@login_required
def order_delete(request):
    args = json.loads(request.body)
    obj = Order.objects.get(pk=args["product_id"])
    obj.is_delete = 1
    obj.save()
    return JsonResponse(dict(data=obj.base_info()))


@login_required
def order_info(request):
    order_id = int(request.GET.get("order_id") or 0)
    obj = Order.objects.get(pk=order_id)
    data = obj.base_info()
    return JsonResponse(dict(data=data))


class MakeOrder(BaseApi):
    def post(self, request):
        args = json.loads(request.body)
        try:
            product = m = None
            product_id = args.get("product_id")
            if product_id:
                product = Product.objects.get(pk=int(product_id))
            product_model_id = args.get("product_model_id")
            if product_model_id:
                m = ProductModel.objects.get(pk=int(product_model_id))
            if product and m:
                obj = Order()
                snowflake = Snowflake()
                _id = snowflake.generate()
                obj.order_id = _id
                obj.product = product
                obj.name = args.get("name", "")
                obj.phone = args.get("phone", "")
                obj.province = args.get("province", "")
                obj.city = args.get("city", "")
                obj.area = args.get("area", "")
                obj.detail_address = args.get("detail_address", "")
                obj.payment_type = PaymentType.COD
                obj.status = OrderStatus.NORMAL
                obj.save()
            else:
                return JsonResponse(dict(code=-1, message="cannot find product for {}".format(product_id)))
        except ObjectDoesNotExist:
            return JsonResponse(dict(code=-1, message="cannot find product for {}".format(product_id)))
        return JsonResponse(dict(code=1, message="success"))
