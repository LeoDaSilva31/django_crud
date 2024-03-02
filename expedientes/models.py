from django.db import models

# Create your models here.
class Persona(models.Model):
    dni=models.CharField(primary_key=True, max_length=50)
    nombre=models.CharField(max_length=100)
    apellido=models.CharField(max_length=100)