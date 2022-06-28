from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from Lyb.Lybmodels.LybModels import Lyb
from Lyb.Serializer.LybSerializer import LybSerializer


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def lyb_list(request):
    """
    列出所有的code snippet，或创建一个新的snippet。
    """
    if request.method == 'GET':
        print('opopopop')
        LybObjs = Lyb.objects.all()
        serializer = LybSerializer(LybObjs, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = LybSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def lyb_detail(request, pk):
    """
    获取，更新或删除一个 code snippet。
    """
    try:
        LybObj = Lyb.objects.get(pk=pk)
    except Lyb.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = LybSerializer(LybObj)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = LybSerializer(LybObj, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        LybObj.delete()
        return HttpResponse(status=204)