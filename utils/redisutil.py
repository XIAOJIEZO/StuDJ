import redis


def redisutil():
    ip = '10.66.210.170'
    password = 'test123'
    RedisObj = redis.Redis(host=ip, password=password, port=6379, db=0, decode_responses=True)

    return RedisObj
