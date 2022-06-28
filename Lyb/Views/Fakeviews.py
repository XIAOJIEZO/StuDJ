from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response

from Lyb.Lybmodels import fakeobj
from Lyb.Serializer.FakeSerializer import FakeSerializer
from utils.apiresponse import APIResponse


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