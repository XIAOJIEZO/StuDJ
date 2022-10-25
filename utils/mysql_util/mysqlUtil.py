import random

import pymysql


def getBankBin(bankname=''):
    db = pymysql.connect(host='127.0.0.1',
                         user='root',
                         password='123456',
                         database='Lyb')

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    if bankname:
        selectQuery = 'select * from bank_bin where bankname = ' + "'" + bankname + "'"
        print(selectQuery)
    else:
        selectQuery = 'select * from bank_bin'

    cursor.execute(selectQuery)

    data = cursor.fetchall()
    len1 = len(data)

    db.close()

    return data[random.randint(0, len1 - 1)]
