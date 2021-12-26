from django.shortcuts import render

from utils import mobilesha1
from utils import redisutil


def del_limiter_counter(request):
    mobile = {}
    if request.POST:
        mobile["mobile"] = request.POST['mobile']

    if len(mobile) == 1:
        encryp_mobile = mobilesha1.encryp(mobile["mobile"])
        key = 'limiter.Counter.' + encryp_mobile

        r = redisutil.redisutil()
        print("请求次数：", r.get(key))
        r.set(key, value=0)

        return render(request, "clear_verification_code_limit.html")

    else:
        return render(request, "clear_verification_code_limit.html")
