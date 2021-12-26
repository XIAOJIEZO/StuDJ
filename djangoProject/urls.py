"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

import testP.api.generate_user_information
from testP.api import clear_verification_code_limit, index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ClearMobileLimit/', clear_verification_code_limit.del_limiter_counter),
    path('index/', index.index_page),
    path('generate_user_information/', testP.api.generate_user_information.generate_user_information),
]
