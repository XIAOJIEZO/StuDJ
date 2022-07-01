from Lyb.Serializer.LybSerializer import LybSerializer
from Lyb.Lybmodels.LybModels import Lyb
from utils.base_model_view_set import BaseModelViewSet
from utils.pagination import CarPageNumberPagination


class LybViewSetList(BaseModelViewSet):

    pagination_class = CarPageNumberPagination
    queryset = Lyb.objects.all().order_by('id')
    serializer_class = LybSerializer

    def lyb_list(self, request, *args, **kwargs):
        CarPageNumberPagination.page_size = request.data.get('pagesize')
        CarPageNumberPagination.pageN = request.data.get('page')

        return self.list(request, *args, **kwargs)
