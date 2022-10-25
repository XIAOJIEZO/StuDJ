from django.views.decorators.csrf import csrf_exempt
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view, action

from Fake.FakeModels import fakeobj
from Fake.Serializer.FakeSerializer import FakeSerializer
from utils.apiresponse import APIResponse

request_body = openapi.Schema(type=openapi.TYPE_OBJECT,
                              required=['locale'],
                              properties={
                                  'locale': openapi.Schema(type=openapi.TYPE_STRING, description='zh_CN zh_TW en'
                                                                                                 '_US ja_JP')})


@swagger_auto_schema(method='post', request_body=request_body)
# @action(methods=['post'], detail=False, )
@csrf_exempt
@api_view(['POST'])
def fakeinfo(request):
    locale = request.data.get('locale')
    bankName = request.data.get('bankName')


    # if bankName:
    #     pass
    # else:
    #     bankName = '招商银行'


    if locale:
        fake = fakeobj.FakeInfo(locale=locale, bankName=bankName)
        serializer = FakeSerializer(fake)
        return APIResponse(data=serializer.data, data_msg=status.HTTP_200_OK, code='ok')

    fake = fakeobj.FakeInfo(bankName=bankName)
    serializer = FakeSerializer(fake)
    return APIResponse(data=serializer.data, data_msg=status.HTTP_200_OK, code='ok')
