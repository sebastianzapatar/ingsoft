from django.contrib import admin
from django.urls import include,path
from home.views import Home,InsertarCancion
urlpatterns=[
    path('',Home.as_view(),name='home'),
    path('new',InsertarCancion.as_view(),name='nueva'),
]