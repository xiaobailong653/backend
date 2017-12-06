# -*- coding: utf-8 -*-
import json
from django.http import HttpResponse
from django.http import JsonResponse
from utils.snowflake import Snowflake
from _base import BaseApi


__author__ = 'Sunlf'


class FileUpload(BaseApi):
    def post(self, request):
        file_type = request.GET.get("file_type")
        file_content = request.body
        if file_content:
            snowflake = Snowflake()
            file_id = snowflake.generate()
            try:
                fname = open("storage/{0}s/{1}.{0}".format(file_type, file_id), "w")
                fname.write(file_content)
                fname.close()
                print file_id
                return JsonResponse({"code": 1, "msg": "success", "data": str(file_id)})
            except Exception as ex:
                print "Upload file except, ex=", ex

        return JsonResponse({"code": -1, "msg": "failure"})


class FileInfo(BaseApi):
    def get(self, request):
        filename = request.GET.get("filename")
        file_path = "storage/images/{0}".format(filename)
        data = open(file_path).read()
        response = HttpResponse(data)
        response['Content-Disposition'] = 'attachment;filename="{}"'.format(filename)
        return response
