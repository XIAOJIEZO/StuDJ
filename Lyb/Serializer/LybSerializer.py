#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/25 10:20
# @Author  : XIAOJIEZI
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/24 10:01
# @Author  : XIAOJIEZI

from rest_framework import serializers
from rest_framework.views import APIView

from Lyb.Lybmodels.LybModels import Lyb
from utils.apiresponse import APIResponse


class LybSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Lyb
        # fields = '__all__'
        fields = ('title', 'author', 'content')

