from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def bienvenida(request):
    return HttpResponse("¡Bienvenido a la aplicación de expedientes!")