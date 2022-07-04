#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/7/1 14:39
# @Author  : XIAOJIEZI
from rest_framework import viewsets
from utils.apiresponse import APIResponse


class LybModelViewSet(viewsets.ModelViewSet):

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        print(response.data)
        return APIResponse(data=response.data)

    def retrieve(self, request, *args, **kwargs):
        response = super().retrieve(request, *args, **kwargs)
        return APIResponse(response.data)

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        # make sure to catch 404's below
        obj = queryset.get(pk=self.request.data.get('id'))
        self.check_object_permissions(self.request, obj)
        return obj
