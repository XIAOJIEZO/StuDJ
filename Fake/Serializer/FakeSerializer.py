#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/24 17:24
# @Author  : XIAOJIEZI
from rest_framework import serializers


class FakeSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    phoneNumber = serializers.CharField(max_length=50)
    idCard = serializers.CharField(max_length=50)
    # birthday = serializers.CharField(max_length=50)
    age = serializers.CharField(max_length=50)
    address = serializers.CharField(max_length=50)
    email = serializers.CharField(max_length=50)
    company = serializers.CharField(max_length=50)
    bankName = serializers.CharField(max_length=50)
    bankCardNumber = serializers.CharField(max_length=50)
    birthday = serializers.DateField


