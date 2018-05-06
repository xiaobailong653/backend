# -*- coding: utf-8 -*-
from django.conf.urls import url
from dianbing.apis import (
    api_product,
    api_order,
    api_upload,
)


urlpatterns = [
    url(r'^product/type/$', api_product.ProductInfo.as_view()),
    url(r'^product/info/$', api_product.ProductInfo.as_view()),
    url(r'^order/make/$', api_order.MakeOrder.as_view()),
    url(r'^file/image/$', api_upload.FileInfo.as_view()),
]
