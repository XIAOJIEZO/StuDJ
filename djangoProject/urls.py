"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to Views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function Views
    1. Add an import:  from my_app import Views
    2. Add a URL to urlpatterns:  path('', Views.home, name='home')
Class-based Views
    1. Add an import:  from other_app.Views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

import testP.api.generate_user_information
import testP.api.generate_user_information2
from testP.api import clear_verification_code_limit, index

from Lyb import Views
from Lyb.Views.LybView3 import lyb_detail3, lyb_list3, lyb_updata, LybDetailView
from Lyb.Views.Fakeviews import fakeinfo
from Lyb.Views import Lybviews
from Lyb.Views.LybView2 import lyb_list, lyb_detail

lybrouter = routers.DefaultRouter()
lybrouter.register(r'lyb', Views.Lybviews.LybViewSet)
lybrouter.register(r'lyb2', Views.Lybviews.LybViewSet2)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ClearMobileLimit/', clear_verification_code_limit.del_limiter_counter),
    path('index/', index.index_page),
    path('generate_user_information/', testP.api.generate_user_information.generate_user_information),
    path('generate_user_information1/', testP.api.generate_user_information2.generate_user_information1),
    path('generate_user_information2/', testP.api.generate_user_information2.generate_user_information2),
    url(r'generate_user_information3/', testP.api.generate_user_information2.generate_user_information3),
    # url(r'^$', TemplateView.as_view(template_name="index.html")),
    # url('userInfo', userinfo),

    url(r'api/', include(lybrouter.urls)),

    url(r'lyb_list2', lyb_list),
    url(r'^lyb_detail2/(?P<pk>[0-9]+)/$', lyb_detail),

    url(r'lyb_list3', lyb_list3),
    url(r'^lyb_detail3/(?P<pk>[0-9]+)/$', lyb_detail3),
    url(r'lyb_updata', lyb_updata),
    url(r'fakeinfo', fakeinfo),

    url(r'get', LybDetailView.get),
    url(r'put', LybDetailView.put),
    url(r'delete', LybDetailView.delete),
    url(r'list', LybDetailView.list),

]
