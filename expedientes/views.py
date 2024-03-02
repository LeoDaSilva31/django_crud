from django.http import HttpResponse
from django.shortcuts import render
from .models import Persona



# Create your views here.
def bienvenida(request):
    personas= Persona.objects.all()
    return render(request, "lista.html", {"persona": personas})

def cargar(request):
    return render(request, "cargar.html")
