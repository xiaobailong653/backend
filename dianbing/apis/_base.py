# -*- coding: utf-8 -*-
import json
from rest_framework.views import APIView
from django.http import JsonResponse
from django.conf import settings
import hashlib


class BaseApi(APIView):

    def get(self, request, *args, **kwargs):

        return JsonResponse(dict(code=-1, message="Method not found"))

    def post(self, request, *args, **kwargs):

        return JsonResponse(dict(code=-1, message="Method not found"))

    def get_arguments(self, request):
        sign = request.META.get("HTTP_SIGN", 0)
        args = json.loads(request.body)
        keys = sorted(args.keys())
        appsecret = settings.APPSECRET
        s = appsecret
        for key in keys:
            s += "{}{}".format(args[key].encode("utf-8"), key)
        s += appsecret
        m = hashlib.md5()
        m.update(s)
        psw = m.hexdigest()
        if sign == psw:
            return args
        return None
