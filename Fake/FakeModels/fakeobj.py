#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/26 14:02
# @Author  : XIAOJIEZI

from faker import Faker
from utils.BankCardNumber import GetBankCardNumber
from utils.id_number_util.identity import IdNumber


class FakeInfo(object):

    def __init__(self, bankName, locale='zh_CN'):

        self.locale = locale
        self.bankName = bankName
        self.name = ""
        self.ssn = ""
        self.phoneNumber = ""
        self.address = ""
        self.bankCardNumber = ""
        self.company = ""
        self.email = ""
        self.job = ""
        self.birthday = ""
        self.age = ""
        self.idCard = ""

        self.getBankCardNumber = lambda: GetBankCardNumber().getBankCardNumber(bankName=self.bankName)
        self.getfake = lambda: Faker(locale=self.locale)

        self.test()

    #
    # def getBankCardNumber(self):
    #     return GetBankCardNumber().getBankCardNumber(bankName=self.bankName)

    # def getfake(self):
    #     return Faker(locale=self.locale)
    def test(self):
        idCard = IdNumber.generate_id()
        self.name = self.getfake().name()
        # self.ssn = self.getfake().ssn()
        self.idCard = idCard
        # self.address = self.getfake().address()
        self.address = IdNumber(idCard).get_area_name()
        self.birthday = IdNumber(idCard).get_birthday()
        self.age = IdNumber(idCard).get_age()
        self.company = self.getfake().company()
        self.email = self.getfake().email()
        self.phoneNumber = self.getfake().phone_number()
        self.bankCardNumber = self.getBankCardNumber()

