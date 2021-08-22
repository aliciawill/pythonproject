"""djangoProject7 URL Configuration

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

import shop01.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', shop01.views.index),
    path('shop01/', shop01.views.start),
    path('shop01/index1', shop01.views.index1),
    path('shop01/index2', shop01.views.index2),
    path('shop01/index0', shop01.views.index0),
    path('shop01/index3', shop01.views.index3),
    path('shop01/index4', shop01.views.index4),
    path('shop01/index5', shop01.views.index5),
    path('shop01/index6', shop01.views.index6),
    path('shop01/index7', shop01.views.index7),
    path('shop01/index8', shop01.views.index8),
    path('shop01/index9', shop01.views.index9),
    path('shop01/index10', shop01.views.index10),
    path('shop01/index11', shop01.views.index11),
    path('shop01/index12', shop01.views.index12),
    path('shop01/index13', shop01.views.index13),
    path('shop01/index14', shop01.views.index14),
    path('shop01/index15', shop01.views.index15),
]
