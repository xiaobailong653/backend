# -*- coding: utf-8 -*-
import json
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from dianbing.models import (
    Order,
    Product,
    OrderStatus,
    PaymentType,
)
from utils.snowflake import Snowflake
from django.core.paginator import (
    Paginator,
    PageNotAnInteger,
    EmptyPage)
from _base import BaseApi


__author__ = 'Sunlf'


class OrderList(BaseApi):
    def get(self, request):
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


class OrderInfo(BaseApi):
    def get(self, request):
        order_id = long(request.GET.get("order_id") or 0)
        try:
            obj = Order.objects.get(order_id=order_id)
            data = obj.base_info()
            print data
        except ObjectDoesNotExist:
            data = {}
        return JsonResponse(dict(data=data))


class MakeOrder(BaseApi):
    def post(self, request):
        # args = self.get_arguments(request)
        args = json.loads(request.body)
        if args:
            try:
                product = None
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
                    obj.product_model = args.get("product_model", "")
                    obj.payment_type = PaymentType.COD
                    obj.status = OrderStatus.NORMAL
                    obj.save()
                else:
                    return JsonResponse(dict(code=-1, message="cannot find product for {}".format(product_id)))
            except ObjectDoesNotExist:
                return JsonResponse(dict(code=-1, message="cannot find product for {}".format(product_id)))
            return JsonResponse(dict(code=1, message="success"))
        else:
            return JsonResponse(dict(code=0, message="invalid request"))
