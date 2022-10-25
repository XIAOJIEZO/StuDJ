#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/26 14:02
# @Author  : XIAOJIEZI

from faker import Faker
from utils.bank_card_utils.BankCardNumber import GetBankCardNumber
from utils.id_number_util.identity import IdNumber


class FakeInfo(object):

    def __init__(self, bankName , locale='zh_CN'):

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
        self.areaId = ""

        self.getBankCardNumber = lambda: GetBankCardNumber()
        self.getfake = lambda: Faker(locale=self.locale)

        self.run()

    #
    # def getBankCardNumber(self):
    #     return GetBankCardNumber().getBankCardNumber(bankName=self.bankName)

    # def getfake(self):
    #     return Faker(locale=self.locale)
    def run(self):
        idCard = IdNumber.generate_id()

        idObj = IdNumber(idCard)

        self.name = self.getfake().name()
        # self.ssn = self.getfake().ssn()
        self.idCard = idCard
        # self.address = self.getfake().address()
        self.address = idObj.get_area_name()
        self.birthday = idObj.get_birthday()
        self.age = idObj.get_age()
        # self.areaId = idObj.area_id()
        self.company = self.getfake().company()
        self.email = self.getfake().email()
        self.phoneNumber = self.getfake().phone_number()
        self.bankCardNumber = self.getBankCardNumber().getBankCardNumber(bankName=self.bankName)[0]
        self.bankName = self.getBankCardNumber().getBankCardNumber(bankName=self.bankName)[1]

