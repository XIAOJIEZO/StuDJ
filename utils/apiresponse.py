#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/27 14:03
# @Author  : XIAOJIEZI
from rest_framework.response import Response


class APIResponse(Response):
    def __init__(self, data=None, data_msg=None, results=None
                 , http_status=None, headers=None, exception=False, code=None, **kwargs):

        # data的初始状态：状态码与状态信息
        data = {
            'code': code,
            'msg': data_msg,
            'data': data,
        }
        # data的响应数据体
        # results可能是False、0等数据，这些数据某些情况下也会作为合法数据返回
        if results is not None:
            data['results'] = results
        # data响应的其他内容
        # if kwargs is not None:
        #     for k, v in kwargs:
        #         setattr(data, k, v)
        data.update(kwargs)

        # 重写父类的Response的__init__方法

        super().__init__(data=data, status=http_status, headers=headers, exception=exception)