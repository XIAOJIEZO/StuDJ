#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/20 16:06
# @Author  : XIAOJIEZI

from utils import fake
from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import json



def generate_user_information1(request):


        user = fake.Users().generate_users()

        return HttpResponse(json.dumps(user))

@csrf_exempt
def generate_user_information2(request):

        par = request.POST["optional"]

        if par == '1':

                user = fake.Users().generate_users()

                return HttpResponse(json.dumps(user))

        else:
                return HttpResponse('wrong request parameter')


@csrf_exempt
def generate_user_information3(request):

        par = json.loads(request.body)

        if par["optional"] == '1':

                user = fake.Users().generate_users()

                return HttpResponse(json.dumps(user))

        else:
                return HttpResponse('wrong request parameter')


