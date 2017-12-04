# -*- coding: utf-8 -*-
from django.conf.urls import url
from dianbing.views import views_route
from dianbing.apis import (
    api_user,
    api_product,
    api_order,
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


urlpatterns += [
    url(r'^api/product/list/$', api_product.product_list),
    url(r'^api/product/info/$', api_product.product_info),
    url(r'^api/product/create/$', api_product.product_create),
    url(r'^api/product/update/$', api_product.product_update),
    url(r'^api/product/delete/$', api_product.product_delete),
    url(r'^api/product/mini/list/$', api_product.product_mini_list),
]


urlpatterns += [
    url(r'^api/order/list/$', api_order.order_list),
    url(r'^api/order/info/$', api_order.order_info),
    url(r'^api/order/create/$', api_order.order_create),
    url(r'^api/order/update/$', api_order.order_update),
    url(r'^api/order/delete/$', api_order.order_delete),
    url(r'^api/order/make/$', api_order.MakeOrder.as_view()),
]
