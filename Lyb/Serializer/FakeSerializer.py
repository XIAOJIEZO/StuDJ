#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/24 17:24
# @Author  : XIAOJIEZI
from rest_framework import serializers


class FakeSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    ssn = serializers.CharField(max_length=50)
    phone_number = serializers.CharField(max_length=50)

