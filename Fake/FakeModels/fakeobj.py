#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/26 14:02
# @Author  : XIAOJIEZI

from faker import Faker
from utils.BankCardNumber import GetBankCardNumber


class FakeInfo(object):

    def __init__(self, bankName, locale='zh_CN'):

        self.locale = locale
        self.bankName = bankName
        self.name = ""
        self.ssn = ""
        self.PhoneNumber = ""
        self.address = ""
        self.BankCardNumber = ""

        self.getBankCardNumber = lambda: GetBankCardNumber().getBankCardNumber(bankName=self.bankName)
        self.getfake = lambda: Faker(locale=self.locale)

        self.test()

    #
    # def getBankCardNumber(self):
    #     return GetBankCardNumber().getBankCardNumber(bankName=self.bankName)

    # def getfake(self):
    #     return Faker(locale=self.locale)

    def test(self):
        self.name = self.getfake().name()
        self.ssn = self.getfake().ssn()
        self.PhoneNumber = self.getfake().phone_number()
        self.BankCardNumber = self.getBankCardNumber()
