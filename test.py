#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/22 17:13
# @Author  : XIAOJIEZI
import requests

r = requests.get('http://127.0.0.1:8000/generate_user_information1/')

print(r.json())