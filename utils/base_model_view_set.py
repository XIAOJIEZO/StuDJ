#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/7/1 14:39
# @Author  : XIAOJIEZI
from rest_framework import viewsets
from rest_framework.response import Response

from utils.apiresponse import APIResponse


class BaseModelViewSet(viewsets.ModelViewSet):
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        return APIResponse(response.data)
