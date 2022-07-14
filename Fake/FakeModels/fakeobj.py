#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/26 14:02
# @Author  : XIAOJIEZI

from faker import Faker

from utils.BankCardNumber import GetBankCardNumber


class FakeInfo(object):

    def __init__(self, bankName, locale='zh_CN'):
        self.locale = locale
        self.name = ""
        self.ssn = ""
        self.PhoneNumber = ""
        self.address = ""
        self.BankCardNumber = ""

        self.bankName = bankName


        # self.get_BankCardNumber = lambda bankName: GetBankCardNumber().getBankCardNumber(bankName=self.bankName)

        self.test()

    #
    def get_BankCardNumber(self):
        return GetBankCardNumber().getBankCardNumber(bankName=self.bankName)

    def get_fake(self):
        return Faker(locale=self.locale)


    def test(self):
        self.name = self.get_fake().name()
        self.ssn = self.get_fake().ssn()
        self.PhoneNumber = self.get_fake().phone_number()
        self.BankCardNumber = self.get_BankCardNumber()
