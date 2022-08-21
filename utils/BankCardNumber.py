import random
import json


class GetBankCardNumber(object):
    def __init__(self):
        self.binNum = ""
        self.midNum = ""
        self.lastCode = ""
        self.bankCardNumber = ""
        self.bankName = ""

    def getBinNum(self, bankName):
        bankToBin = json.load(open("utils/config/banknametobin.json", encoding="utf-8"))
        if bankName:
            self.binNum = bankToBin[bankName]
            return bankToBin[bankName]
        else:
            tempBank = random.sample(bankToBin.keys(), 1)[0]
            self.binNum = bankToBin[tempBank]
            return self.binNum, tempBank

    def getMidNum(self, bankName):

        bankList = ('工商银行', '中国银行')

        tempMidnum = ""

        if bankName in bankList:

            for x in range(9):
                tempMidnum = tempMidnum + str(random.randint(0, 12))
                x = x
            self.midNum = tempMidnum

            return self.midNum

        else:

            for x in range(9):
                tempMidnum = tempMidnum + str(random.randint(0, 9))
                x = x
            self.midNum = tempMidnum

            return self.midNum

    def getLastcode(self, bankNumNoLastcode):
        sum = 0
        for i in bankNumNoLastcode[-1::-2]:
            for m in str(int(i) * 2):
                sum = sum + int(m)
        for j in bankNumNoLastcode[-2::-2]:
            sum = sum + int(j)
        if sum % 10 == 0:
            self.lastCode = '0'
        else:
            self.lastCode = str(10 - sum % 10)
        return self.lastCode

    def getBankCardNumber(self, bankName):

        if bankName:
            self.getBinNum(bankName)
            self.getMidNum(bankName)

        else:
            self.getBinNum(bankName)
            self.getMidNum()
        self.getLastcode(self.binNum + self.midNum)
        self.bankCardNumber = self.binNum + self.midNum + self.lastCode
        return self.bankCardNumber
