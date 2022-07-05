#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/7/1 14:39
# @Author  : XIAOJIEZI
from rest_framework import viewsets, status

from utils.apiresponse import APIResponse


class LybModelViewSet(viewsets.ModelViewSet):

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        return APIResponse(data=response.data, code=response.status_code, data_msg=response.status_text)

    def retrieve(self, request, *args, **kwargs):
        response = super().retrieve(request, *args, **kwargs)
        return APIResponse(response.data, code=response.status_code, data_msg=response.status_text)

    # def destroy(self, request, *args, **kwargs):
    #     response = super().destroy(request, *args, **kwargs)
    #     return APIResponse(data=response.data, code=response.status_code, data_msg=response.status_text)

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

    def update(self, request, *args, **kwargs):
        try:
            if request.data.get('id') == None:
                response = super().create(request, *args, **kwargs)
                return APIResponse(response.data, code=response.status_code, data_msg=response.status_text)

            response = super().update(request, *args, **kwargs)
            return APIResponse(response.data, code=response.status_code, data_msg=response.status_text)
        except Exception as e:
            return APIResponse(code=status.HTTP_400_BAD_REQUEST, data_msg=e.__str__())

    # def destroy(self, request, *args, **kwargs):
    #     # try:
    #     #     if request.data.get('id') == None:
    #     #         return APIResponse('id matching query does not exist.1')
    #     #     self.queryset.is_delete = True
    #     #     self.queryset.save()
    #     #
    #     #     return APIResponse('Successful operation')
    #     # except Exception as e:
    #     #     print(e)
    #     #     return APIResponse('id matching query does not exist.2')
    #
    #         instance = self.get_object()
    #         instance.is_delete = True
    #         return APIResponse(status=status.HTTP_204_NO_CONTENT)

    """
    Destroy a model instance.
    """

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return APIResponse(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()
        instance.is_delete = True
