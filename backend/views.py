# -*- coding: utf-8 -*-
import json
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.http import JsonResponse


@login_required
def index(request):
    return render_to_response("index.html")


def login(request):
    if request.method == "POST":
        data = json.loads(request.body)
        username = data.get("username")
        password = data.get("password")
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            return JsonResponse(dict(code=1, message="success"))
        return JsonResponse(dict(code=-1, message="Unknown username or bad password"))
    else:
        return render_to_response("login.html")


@login_required
def logout(request):
    auth.logout(request)
    return JsonResponse(dict(code=1, message="Logout"))
