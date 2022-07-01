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
from django.urls import path, include, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

import testP.api.generate_user_information
import testP.api.generate_user_information2
from testP.api import clear_verification_code_limit, index


schema_view = get_schema_view(
    openapi.Info(
        title='API接口文档',
        default_version='v1',
        description='接口文档平台',
        # terms_of_service='http://api.xxx.com',
        contact=openapi.Contact(email='xxxx@qq.com'),
        license=openapi.License(name='License')
    ),
    public=True
    # 权限类
    # permission_classes = (permissions.AllowAny),
)

urlpatterns = [

    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('admin/', admin.site.urls),
    path('ClearMobileLimit/', clear_verification_code_limit.del_limiter_counter),
    path('index/', index.index_page),
    path('generate_user_information/', testP.api.generate_user_information.generate_user_information),
    path('generate_user_information1/', testP.api.generate_user_information2.generate_user_information1),
    path('generate_user_information2/', testP.api.generate_user_information2.generate_user_information2),
    url(r'generate_user_information3/', testP.api.generate_user_information2.generate_user_information3),
    # url(r'^$', TemplateView.as_view(template_name="index.html")),
    # url(r'^lyb_detail2/(?P<pk>[0-9]+)/$', lyb_detail),

    path(r'fake/', include("Fake.urls")),

    path(r'lyb/', include("Lyb.urls"))

]
