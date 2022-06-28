from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from Lyb.Lybmodels.LybModels import Lyb
from Lyb.Serializer.LybSerializer import LybSerializer
from utils.apiresponse import APIResponse


@csrf_exempt
@api_view(['GET'])
def lyb_list3(request):
    if request.method == 'GET':
        LybObjs = Lyb.objects.all().order_by('-create_time')
        serializer = LybSerializer(LybObjs, many=True)
        return APIResponse(serializer.data)


@csrf_exempt
@api_view(['GET'])
def lyb_detail3(request, pk):
    try:
        LybObj = Lyb.objects.get(pk=pk)
    except Lyb.DoesNotExist:
        return APIResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = LybSerializer(LybObj)
        return APIResponse(serializer.data)


@csrf_exempt
@api_view(['POST'])
def lyb_updata(request):
    if request.method == 'POST':

        try:
            LybObj = Lyb.objects.get(pk=request.data['id'])
            LybObj.title = request.data['title']
            LybObj.author = request.data['author']
            LybObj.content = request.data['content']
            LybObj.save()
            return APIResponse(request.data)

        except:
            serializer = LybSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return APIResponse(serializer.data, status=status.HTTP_201_CREATED)
            return APIResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LybDetailView(APIView):

    # 单条数据的查看
    @csrf_exempt
    @api_view(['POST'])
    def get(request):

        try:
            lyb = Lyb.objects.filter(pk=request.data["id"])
            if lyb.exists():
                bs = LybSerializer(lyb.first())  # 序列化model对象
                return APIResponse(bs.data)

            return APIResponse(data_msg='id matching query does not exist.', status=status.HTTP_200_OK)

        except Exception as e:
            return APIResponse(data_msg=str(e), status=status.HTTP_200_OK)

    # 单条数据的更新
    @csrf_exempt
    @api_view(['POST'])
    def put(request):

        try:
            lyb = Lyb.objects.filter(pk=request.data["id"])
            if lyb.exists():
                bs = LybSerializer(lyb.first(), data=request.data)
                if bs.is_valid():  # 校验put请求提交的数据
                    bs.save()  # update操作
                    return APIResponse(bs.data, status=status.HTTP_200_OK)
                else:
                    return APIResponse(bs.errors, status.HTTP_201_CREATED)

            return APIResponse(data_msg='id matching query does not exist.')

        except KeyError:
            serializer = LybSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return APIResponse(serializer.data, status=status.HTTP_201_CREATED)
            return APIResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return APIResponse(data_msg=str(e))

    # # 单条数据的删除
    @csrf_exempt
    @api_view(['POST'])
    def delete(request):

        try:
            lyb = Lyb.objects.filter(pk=request.data["id"])
            lyb_first = lyb.first()

            if lyb.exists() and lyb_first.is_delete == False:
                # book = Lyb.objects.filter(pk=request.data["id"]).delete()
                lyb_first.is_delet = True
                lyb_first.save()
                return APIResponse("successfully deleted", status=status.HTTP_200_OK)

            return APIResponse(data_msg='id matching query does not exist.', status=status.HTTP_200_OK)

        except KeyError:
            return APIResponse(data_msg='id matching query does not exist.', status=status.HTTP_200_OK)

        except Exception as e:
            return APIResponse(data_msg=str(e), status=status.HTTP_200_OK)

    @csrf_exempt
    @api_view(['POST'])
    def list(request):
        if request.method == 'POST':
            LybObjs = Lyb.objects.all().order_by('-create_time')
            serializer = LybSerializer(LybObjs, many=True)
            return APIResponse(serializer.data)

