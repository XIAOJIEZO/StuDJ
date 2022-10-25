from django.views.decorators.csrf import csrf_exempt
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view
from Fake.FakeModels import cache_refresh

# @action(methods=['post'], detail=False, )
from utils.apiresponse import APIResponse


@csrf_exempt
@api_view(['POST'])
def cacheRefresh(request):
    try:
        cache_refresh.test777()
        return APIResponse(data_msg=status.HTTP_200_OK, code='ok')

    except Exception as e:
        return APIResponse(data=e, data_msg=status.HTTP_200_OK, code='ok')
