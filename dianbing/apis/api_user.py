# -*- coding: utf-8 -*-
import json
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from dianbing.models import Sakesman
from utils.timetool import TimeHandler
from django.core.paginator import (
    Paginator,
    PageNotAnInteger,
    EmptyPage)


__author__ = 'Sunlf'


@login_required
def user_list(request):
    page = request.GET.get("index", 1)
    size = request.GET.get("size", 20)
    spec = dict(is_delete=0)
    if request.GET.get("name"):
        spec["name"] = request.GET.get("name")

    objects = User.objects.all()
    paginator = Paginator(objects, size)
    try:
        records = paginator.page(page)
    except PageNotAnInteger:
        records = paginator.page(1)
    except EmptyPage:
        records = paginator.page(paginator.num_pages)
    data = []
    for record in records:
        data.append(dict(user_id=record.id,
                         user_name=record.username,
                         group_name="白起团队",
                         create_time=record.date_joined))
    return JsonResponse(dict(data=data, total=paginator.count))


@login_required
def user_info(request):
    user = request.user
    data = dict(user_id=user.id,
                user_name=user.username)
    return JsonResponse(dict(data=data))


@login_required
def user_create(request):
    args = json.loads(request.body)
    sake = Sakesman()
    obj = User()
    obj.username = args.get("username", "")
    obj.password = args.get("password", "")
    obj.email = args.get("email", "")
    obj.phone = args.get("phone", 0)
    obj.save()
    sake.user = obj
    sake.phone = args.get("phone", 0)
    sake.save()
    return JsonResponse(dict(data=0))

@login_required
def user_update(request):
    username = request.POST.get("username", 1)
    password = request.POST.get("password", 20)
