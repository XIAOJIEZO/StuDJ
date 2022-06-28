#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/25 10:19
# @Author  : XIAOJIEZI
from django.db import models


# Create your Lybmodels here.


# class BaseModel(models.Model):
#     is_delete = models.BooleanField(default=False)
#     create_time = models.DateTimeField(auto_now_add=True)
#
#
# class Lyb(BaseModel):
#     title = models.CharField(max_length=20, verbose_name='标题')
#     author = models.CharField(max_length=20, verbose_name='作者')
#     content = models.TextField()
#
#     class Meta:
#         db_table = 'd_lyb'