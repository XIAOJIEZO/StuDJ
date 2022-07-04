#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/7/1 14:39
# @Author  : XIAOJIEZI
from rest_framework import viewsets

from utils.apiresponse import APIResponse


class LybModelViewSet(viewsets.ModelViewSet):

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        return APIResponse(data=response.data, code=response.status_code, data_msg=response.status_text)

    def retrieve(self, request, *args, **kwargs):
        response = super().retrieve(request, *args, **kwargs)
        return APIResponse(response.data)

    def destroy(self, request, *args, **kwargs):
        response = super().destroy(request, *args, **kwargs)
        return APIResponse(data=response.data, code=response.status_code, data_msg=response.status_text)

    # def update(self, request, *args, **kwargs):
    #     response = super().update(request, *args, **kwargs)
    #     return APIResponse(data=response.data, code=response.status_code, data_msg=response.status_text)
    #
    # def create(self, request, *args, **kwargs):
    #     response = super().create(request, *args, **kwargs)
    #     return APIResponse(data=response.data, code=response.status_code, data_msg=response.status_text)

    def get_object(self):

        queryset = self.filter_queryset(self.get_queryset())
        obj = queryset.get(pk=self.request.data.get('id'))
        self.check_object_permissions(self.request, obj)
        return obj

    def test(self, request, *args, **kwargs):
        try:
            if request.data.get('id') == None:
                return self.create(request, *args, **kwargs)
            return self.update(request, *args, **kwargs)
        except:
            return APIResponse('id matching query does not exist.')
