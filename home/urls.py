# -*- coding: utf-8 -*-

from django.urls import path
from django.conf.urls import url

from .import views

urlpatterns=[

    path('',views.index,name='index'),

    #path('home',views.home,name='home'),
    #url(r'^register/$',views.register),

    path('register',views.register, name='register'),

    path('login', views.login, name='login'),
    #path('add',views.add, name='add')

    path('logout', views.logout, name='logout')

]