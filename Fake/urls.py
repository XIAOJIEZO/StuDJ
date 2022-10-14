#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/29 8:51
# @Author  : XIAOJIEZI
from os import path

from django.conf.urls import url
from Fake.Views.Fakeviews import fakeinfo
from Fake.Views.cacheRefreshViews import cacheRefresh

urlpatterns = [

    url(r'fakeinfo', fakeinfo),
    url(r'cacheRefresh', cacheRefresh),

]