"""wohou URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from banner import views as banner_views
from rest_framework.authtoken import views as authtoken_views
from account import views as account_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-token-auth/', authtoken_views.obtain_auth_token),
    url(r'^register', account_views.AccountRegisterAPIView.as_view()),
    url(r'^reset_password', account_views.RestPasswordView.as_view()),

    url(r'^accounts/$', account_views.AccountList.as_view()),
    url(r'^accounts/(?P<pk>[0-9]+)/$', account_views.AccountDetail.as_view()),

    url(r'^banners/$', banner_views.BannerList.as_view()),
    url(r'^banners/(?P<pk>[0-9]+)/$', banner_views.BannerDetail.as_view()),

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]

