# -*- coding: utf-8 -*-
import json
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from dianbing.models import Product
from django.core.paginator import (
    Paginator,
    PageNotAnInteger,
    EmptyPage)
from _base import BaseApi
from django.views.decorators.csrf import csrf_exempt

__author__ = 'Sunlf'


class ProductList(BaseApi):
    def get(self, request):
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
            data.append(record.base_info())
        return JsonResponse(dict(data=data, total=paginator.count))


class ProductInfo(BaseApi):
    def get(self, request):
        product_id = int(request.GET.get("product_id") or 0)
        try:
            obj = Product.objects.get(pk=product_id)
            data = obj.base_info()
        except ObjectDoesNotExist:
            data = {}
        return JsonResponse(dict(data=data))


class ProductCreate(BaseApi):
    @csrf_exempt
    def post(self, request):
        args = json.loads(request.body)
        obj = Product()
        for key in args:
            setattr(obj, key, args[key])
        obj.save()
        return JsonResponse(dict(data=obj.base_info()))


class ProductUpdate(BaseApi):
    def post(self, request):
        args = json.loads(request.body)
        obj = Product.objects.get(pk=args["product_id"])
        for key in args:
            setattr(obj, key, args[key])
        obj.save()
        return JsonResponse(dict(data=obj.base_info()))


class ProductDelete(BaseApi):
    def post(self, request):
        args = json.loads(request.body)
        obj = Product.objects.get(pk=args["product_id"])
        obj.is_delete = 1
        obj.save()
        return JsonResponse(dict(data=obj.base_info()))


class ProductMiniList(BaseApi):
    def get(self, request):
        data = []
        objs = Product.objects.filter(is_delete=0).order_by("-create_time")
        for obj in objs:
            data.append(dict(product_id=obj.product_id,
                             product_name=obj.product_name,))
        return JsonResponse(dict(data=data))
