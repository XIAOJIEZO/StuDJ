# from django.shortcuts import render
#
# # Create your Views here.
from rest_framework import viewsets

from Lyb.Serializer.LybSerializer import LybSerializer
from Lyb.Lybmodels.LybModels import Lyb


class LybViewSet(viewsets.ModelViewSet):

    queryset = Lyb.objects.all().order_by('-id')

    serializer_class = LybSerializer


class LybViewSet2(viewsets.ModelViewSet):

    queryset = Lyb.objects.all().order_by('-create_time')

    serializer_class = LybSerializer



