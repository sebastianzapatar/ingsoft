from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from django.urls import reverse_lazy
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
    
