"""pydcdemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from . import myadmin
from . import foodproduct
from . import cooker
from . import dcapi
urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', myadmin.hello),
    path('test/', myadmin.test),
    path('testdata/', myadmin.testdata),
    path('foodadd/', foodproduct.foodadd),
    path('foodaddpost/', foodproduct.foodaddpost),
    path('foodlist/', foodproduct.foodlist),
    path('foodedit/', foodproduct.foodedit),
    path('foodeditpost/', foodproduct.foodeditpost),
    path('fooddelete/', foodproduct.fooddelete),
    path('pptlist/', foodproduct.pptlist),
    path('pptlistpost/', foodproduct.pptlistpost),
    path('pptdelete/', foodproduct.pptdelete),
    #pptdelete
    path('cookeradd/', cooker.cookeradd),
    path('cookeraddpost/', cooker.cookeraddpost),
    path('cookerlist/', cooker.cookerlist),
    path('cookeredit/', cooker.cookeredit),
    path('cookereditpost/', cooker.cookereditpost),
    path('cookerdelete/', cooker.cookerdelete),

    path('orderlist/', foodproduct.orderlist),
    path('orderdelete/', foodproduct.orderdelete),
    path('orderview/', foodproduct.orderview),
    path('login/', foodproduct.login),
    path('loginpost/', foodproduct.loginpost),

    path('dcapi/login', dcapi.login),
    path('dcapi/getfoodbyid', dcapi.getfoodbyid),
    path('dcapi/getfoodlist', dcapi.getfoodlist),
    path('dcapi/addtocar', dcapi.addtocar),
    path('dcapi/getcarlist', dcapi.getcarlist),
    path('dcapi/changecarnum', dcapi.changecarnum),
    path('dcapi/deleteitembyid', dcapi.deleteitembyid),
    path('dcapi/saveorder', dcapi.saveorder),
    path('dcapi/getcookerlist', dcapi.getcookerlist),
    path('dcapi/getcookerbyid', dcapi.getcookerbyid),
    path('dcapi/getfoodlistbyrandom', dcapi.getfoodlistbyrandom),
    path('dcapi/getcookerlistbyrandom', dcapi.getcookerlistbyrandom),
    path('dcapi/getorderlist', dcapi.getorderlist),
    path('dcapi/getpptlistbyrandom', dcapi.getpptlistbyrandom),
    path('dcapi/zhuce', dcapi.zhuce),

    path('dcapi/getlistmsg', dcapi.getlistmsg),
    path('dcapi/addmsg', dcapi.addmsg)
]
from . import myadmin