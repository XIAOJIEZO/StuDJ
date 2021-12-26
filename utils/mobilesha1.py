import hashlib


def encryp(moblie):
    hash = hashlib.sha1()  # md5对象，md5不能反解，但是加密是固定的，就是关系是一一对应，所以有缺陷，可以被对撞出来
    hash.update(bytes(moblie, encoding='utf-8'))  # 要对哪个字符串进行加密，就放这里
    print("加密字符串：", hash.hexdigest())  # 拿到加密字符串

    return hash.hexdigest()
