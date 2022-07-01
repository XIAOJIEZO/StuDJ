#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/29 8:51
# @Author  : XIAOJIEZI

from django.conf.urls import url
from django.urls import include, path

from Lyb.Views.Lybviews import LybDetailView
from Lyb.Views.Lybviews2 import LybViewSetList

lyb_list = LybViewSetList.as_view({
    'post': 'lyb_list',
})

urlpatterns = [

    path(r'updata', LybDetailView.updata),
    path(r'delete', LybDetailView.delete),
    path(r'detail', LybDetailView.detail),
    path(r'list', LybDetailView.list),
    url(r'list1', lyb_list, name='lyb_list'),

]
