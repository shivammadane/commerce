"""Ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from shopping.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('log/',logi,name='login'),
    path('sign/',signu,name='sign'),
    path('lo/',logou,name='ou'),
    path('abo/',aboutus,name='about'),
    path('con/',contact,name='contact'),
    path('mega/<int:sid>',mega,name='meg'),
    #path('forget/',forget,name='fp'),
    #path('forget1/',forget1,name='fp1'),
    path('prod/<int:pid>/',prodetail,name='prod'),
    path('cart/<int:pid>',addtocarttable,name='cart'),
    path('mycart/',cart,name='mycart'),
    path('removepro/<int:sid>/',remove_from_cart,name='remove'),
    path('ship/<str:cid>/',check,name='ship'),
    path('paymentcheck/<int:order_id>/',payment_check,name='paycheck'),
    path('dashboard/<str:type>',userdashboard,name='dash'),
    path('track/<int:tid>/',track,name='track'),
    path('add_edit/',add_edit,name='ae'),
    path('add_sub/',add_subcat,name='sb'),
    path('add_cat/',add_cat,name='ac'),
    path('edit/<int:pid>/',edit_pro,name='ed'),
    path('delete/<int:did>/<str:type>/',delete_details,name='delete'),
    path('complete/',completed,name='com'),
    path('otherthan/',other,name='oth'),
    path('chngst/<int:idf>/',changestatus,name='change'),
    path('coeent/<int:pid>/',comment,name='co')
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
