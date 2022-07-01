#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/30 10:57
# @Author  : XIAOJIEZI
# !/usr/bin/env python
# _*_ coding:utf-8 _*_


# 自定义分页需要
from rest_framework.pagination import PageNumberPagination


# 自定义普通分页
class CarPageNumberPagination(PageNumberPagination):
    # 默认一页的条数
    page_size = None
    # 用户可以自定义选择一页的条数，但最多显示10条
    page_sizemax_page_size = 10
    # 获取页码数
    page_size_query_param = None

    pageN = None

    def get_page_number(self, request, paginator):
        page_number = self.pageN
        return page_number
