# -*- coding: utf-8 -*-
from django.conf.urls import url
from dianbing.views import views_route
from dianbing.apis import (
    api_user,
    api_product,
    api_order,
    api_upload,
)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^view/(?P<project>\w+)/(?P<view>\w+)/$', views_route),
]

urlpatterns += [
    url(r'^api/user/list/$', login_required(api_user.UserList.as_view())),
    url(r'^api/user/info/$', login_required(api_user.UserInfo.as_view())),
    url(r'^api/user/create/$', login_required(api_user.UserCreate.as_view())),
    url(r'^api/user/update/$', login_required(api_user.UserUpdate.as_view())),
]


urlpatterns += [
    url(r'^api/product/type/(?P<path>\w+)$', login_required(api_product.ProductTypeList.as_view())),
    url(r'^api/product/list/$', login_required(api_product.ProductList.as_view())),
    url(r'^api/product/info/$', login_required(api_product.ProductInfo.as_view())),
    url(r'^api/product/create/$', api_product.ProductCreate.as_view()),
    url(r'^api/product/update/$', login_required(api_product.ProductUpdate.as_view())),
    url(r'^api/product/delete/$', login_required(api_product.ProductDelete.as_view())),
    url(r'^api/product/mini/list/$', login_required(api_product.ProductMiniList.as_view())),
]


urlpatterns += [
    url(r'^api/order/list/$', login_required(api_order.OrderList.as_view())),
    url(r'^api/order/info/$', login_required(api_order.OrderInfo.as_view())),
]

urlpatterns += [
    url(r'^api/upload/file/$', login_required(api_upload.FileUpload.as_view())),
]
