# -*- coding: utf-8 -*-
import json
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from dianbing.models import Product
from utils.timetool import TimeHandler
from django.core.paginator import (
    Paginator,
    PageNotAnInteger,
    EmptyPage)


__author__ = 'Sunlf'


@login_required
def product_list(request):
    page = request.GET.get("index", 1)
    size = request.GET.get("size", 20)
    spec = dict(is_delete=0)
    product_name = request.GET.get("product_name")
    if product_name:
        spec["product_name__icontains"] = product_name
    product_id = request.GET.get("product_id")
    if product_id:
        spec["product_id"] = int(product_id)

    objects = Product.objects.filter(**spec).order_by("-create_time")
    paginator = Paginator(objects, size)
    try:
        records = paginator.page(page)
    except PageNotAnInteger:
        records = paginator.page(1)
    except EmptyPage:
        records = paginator.page(paginator.num_pages)
    data = []
    for record in records:
        data.append(dict(product_id=record.product_id,
                         product_name=record.product_name,
                         price=record.price,
                         stock=record.stock,
                         create_time=record.create_time))
    return JsonResponse(dict(data=data, total=paginator.count))


@login_required
def product_info(request):
    product_id = int(request.GET.get("product_id") or 0)
    obj = Product.objects.get(pk=product_id)
    data = obj.base_info()
    return JsonResponse(dict(data=data))


@login_required
def product_create(request):
    args = json.loads(request.body)
    obj = Product()
    for key in args:
        setattr(obj, key, args[key])
    obj.save()
    return JsonResponse(dict(data=obj.base_info()))


@login_required
def product_update(request):
    args = json.loads(request.body)
    obj = Product.objects.get(pk=args["product_id"])
    for key in args:
        setattr(obj, key, args[key])
    obj.save()
    return JsonResponse(dict(data=obj.base_info()))


@login_required
def product_delete(request):
    args = json.loads(request.body)
    obj = Product.objects.get(pk=args["product_id"])
    obj.is_delete = 1
    obj.save()
    return JsonResponse(dict(data=obj.base_info()))


@login_required
def product_mini_list(request):
    data = []
    objs = Product.objects.filter(is_delete=0).order_by("-create_time")
    for obj in objs:
        data.append(dict(product_id=obj.product_id,
                         product_name=obj.product_name,))
    return JsonResponse(dict(data=data))
