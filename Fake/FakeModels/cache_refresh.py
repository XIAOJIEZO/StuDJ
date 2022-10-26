import requests

portDict = {'sale-master': '49091'}

testIp = '10.60.210.17'

cacheQueryPath = '/actuator/cacheQuery'

cacheRefreshPathBase = '/actuator/cacheRefresh/'


def getCachePath(port):
    cachePathList = []

    resUrl = 'http://' + testIp + ':' + port + cacheQueryPath + '?pageNum=1&pageSize=10000&cacheName='
    res = requests.get(resUrl)

    for cacheName in res.json()['body']['dataList']:
        cachePathList.append(cacheName.get('cacheName'))

    return cachePathList


def cacheRefresh(port):
    cachePathList = getCachePath(port)

    for cachePath in cachePathList:
        resUrl = 'http://' + testIp + ':' + port + cacheRefreshPathBase + cachePath
        print(resUrl)
        res = requests.get(resUrl)
        # resResult = res.json()['code']

        # if resResult == '0':
        #     return res.json()['msg']
        # return res.json()['msg']


def test777():
    for port in portDict.values():
        cacheRefresh(port)


if __name__ == '__main__':
    test777()
