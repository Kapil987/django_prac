"""mysite URL Configuration

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
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name='index'), #home is going to view.index it will got to views.py
    # path('about/',views.about, name='about'), # program will come and look in url patterns and then it will look for name which is
    # about (given in browser) then it will got to view.about (function name in views.py), name is short form for this funciton
    # about
    # path('removepunc/',views.removepunc, name='removepunc'),
    path('analyze',views.analyze, name='analyze'),
    path('about/',views.about, name='about'),
]
