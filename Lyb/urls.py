#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/29 8:51
# @Author  : XIAOJIEZI

from django.conf.urls import url
from django.urls import include
from rest_framework import routers

from Lyb import Views
from Lyb.Views.Lybviews import LybDetailView
router = routers.SimpleRouter()
router.register(r'lyb', Views.Lybviews.LybViewSet)
router.register(r'lyb2', Views.Lybviews.LybViewSet2)

urlpatterns = [

    url(r'', include(router.urls)),

    url(r'list', LybDetailView.list),
    url(r'updata', LybDetailView.updata),
    url(r'delete', LybDetailView.delete),
    url(r'detail', LybDetailView.detail),

]