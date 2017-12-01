# -*- coding: utf-8 -*-
from django.conf.urls import url
from dianbing.views import views_route
from dianbing.apis import (
    api_user,
)

urlpatterns = [
    url(r'^view/(?P<project>\w+)/(?P<view>\w+)/$', views_route),
]

urlpatterns += [
    url(r'^api/user/list/$', api_user.user_list),
    url(r'^api/user/info/$', api_user.user_info),
    url(r'^api/user/create/$', api_user.user_create),
    url(r'^api/user/update/$', api_user.user_update),
]
