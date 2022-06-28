from django.views.decorators.csrf import csrf_exempt
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from rest_framework.response import Response

from Lyb.Lybmodels import fakeobj
from Lyb.Serializer.FakeSerializer import FakeSerializer
from utils.apiresponse import APIResponse

request_body = openapi.Schema(type=openapi.TYPE_OBJECT,
                              required=['locale'],
                              properties={'locale': openapi.Schema(type=openapi.TYPE_STRING, description='zh_CN zh_TW en_US ja_JP')})


@swagger_auto_schema(method='post', request_body=request_body)
@csrf_exempt
@api_view(['POST'])
def fakeinfo(request):
    try:
        locale = request.data['locale']
        fake = fakeobj.FakeInfo(locale)
        serializer = FakeSerializer(fake)
        return APIResponse(serializer.data)

    except KeyError:

        fake = fakeobj.FakeInfo()
        serializer = FakeSerializer(fake)
        return APIResponse(serializer.data)

    except Exception as e:
        return APIResponse(str(e))
