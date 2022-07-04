#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/29 8:51
# @Author  : XIAOJIEZI

from django.conf.urls import url
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from Lyb.Views.Lybviews import LybDetailView
from Lyb.Views.Lybviews2 import LybViewSetList

lyb_list = LybViewSetList.as_view({
    'post': 'lyb_list',
    # 'post': 'lyb_detail',
})

lyb_detail = LybViewSetList.as_view({
    'post': 'lyb_detail',
    # 'post': 'lyb_detail',
})

lyb_update = LybViewSetList.as_view({
    'post': 'lyb_update',
    # 'post': 'lyb_detail',
})

# router = DefaultRouter()
# router.register(r'snippets', LybViewSetList)

urlpatterns = [

    # path(r'updata', LybDetailView.updata),
    # path(r'delete', LybDetailView.delete),
    # path(r'detail', LybDetailView.detail),
    # path(r'list', LybDetailView.list),
    url(r'list1', lyb_list, name='lyb_list'),
    # url(r'^', include(router.urls)),
    url("detail1", lyb_detail, name='lyb_detail'),
    url("update", lyb_update, name='lyb_update')

]
