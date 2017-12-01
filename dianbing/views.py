# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response

__author__ = 'Sunlf'


def views_route(request, project, view):

    return render_to_response("{}/{}.html".format(project, view))
