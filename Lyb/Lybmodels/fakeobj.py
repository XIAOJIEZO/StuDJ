#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/26 14:02
# @Author  : XIAOJIEZI

from faker import Faker


class FakeInfo(object):

    def __init__(self, locale='zh_CN'):
        try:
            fake = Faker(locale=locale)
            self.name = fake.name()
            self.ssn = fake.ssn()
            self.phone_number = fake.phone_number()

        except AttributeError:
            return