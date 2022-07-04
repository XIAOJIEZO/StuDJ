from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import action

from Lyb.Serializer.LybSerializer import LybSerializer
from Lyb.Lybmodels.LybModels import Lyb
from utils.apiresponse import APIResponse
from utils.base_model_view_set import LybModelViewSet
from utils.pagination import CarPageNumberPagination
from rest_framework import viewsets


class LybViewSetList(LybModelViewSet):
    # queryset = Lyb.objects.all().order_by('-id').filter(is_delete=False)
    queryset = Lyb.objects.filter(is_delete=False)
    serializer_class = LybSerializer

    def lyb_list(self, request, *args, **kwargs):
        self.queryset = self.queryset.all().order_by('-id')
        self.pagination_class = CarPageNumberPagination
        self.pagination_class.page_size = request.data.get('pagesize')
        self.pagination_class.pageN = request.data.get('page')

        return self.list(self.queryset, *args, **kwargs)

    def lyb_detail(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def lyb_update(self, request, *args, **kwargs):
        return self.test(request, *args, **kwargs)
