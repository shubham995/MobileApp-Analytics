"""appdecodeweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib.auth.decorators import user_passes_test

import views

login_forbidden =  user_passes_test(lambda u: u.is_anonymous(), '/user/home')

#(?P<id>REGEXP)
urlpatterns = [
    url(r'^home/$', views.home, name='home'),
    url(r'^info/(?P<app_id>[a-zA-Z0-9._]+)/$', views.appinfo, name='info'),
    url(r'^emotions/(?P<app_id>[a-zA-Z0-9._]+)/$', views.emotions, name='emotions'),
    url(r'^ratings/(?P<app_id>[a-zA-Z0-9._]+)/$', views.ratings, name='ratings'),
]
