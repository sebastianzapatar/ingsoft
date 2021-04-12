from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from django.urls import reverse_lazy
from rest_framework import viewsets
from home.serializers import CancionSerializer
from home.models import Cancion
from home.forms import CancionForm


# Create your views here.
class Home1(generic.View):
    def get(self,request,*args,**kwargs):
        return HttpResponse('Clase ing soft')
class Home(generic.ListView):
    model=Cancion
    template_name="home/home.html"
    context_object_name="obj"
class InsertarCancion(generic.CreateView):
    model=Cancion
    template_name="home/insertar.html"
    form_class=CancionForm
    context_object_name="obj"
    success_url=reverse_lazy('home:home')
class EditarCancion(generic.UpdateView):
    model=Cancion
    template_name="home/insertar.html"
    form_class=CancionForm
    context_object_name="obj"
    success_url=reverse_lazy('home:home')
class EliminarCancion(generic.DeleteView):
    model=Cancion
    template_name="home/eliminar.html"
    context_object_name="obj"
    success_url=reverse_lazy('home:home')
class CancionViewSet(viewsets.ModelViewSet):
    queryset=Cancion.objects.all()
    serializer_class=CancionSerializer
