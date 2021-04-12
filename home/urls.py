from django.contrib import admin
from django.urls import include,path
from home.views import Home,InsertarCancion,\
    EditarCancion,EliminarCancion, CancionViewSet
from rest_framework import routers
router=routers.DefaultRouter()
router.register('cancion',CancionViewSet)

urlpatterns=[
    path('',Home.as_view(),name='home'),
    path('new',InsertarCancion.as_view(),name='nueva'),
    path('edit/<int:pk>',EditarCancion.as_view(),name='editar'),
    path('delete/<int:pk>',EliminarCancion.as_view(),name='eliminar'),
    path('api',include(router.urls)),
]