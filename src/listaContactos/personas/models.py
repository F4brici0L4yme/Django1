from django.db import models

# Create your models here.
class Persona(models.Model):
    nombres = models.CharField(max_length=100, blank=False)
    apellidos = models.CharField(max_length=100, blank=False)
    edad = models.CharField(max_length=3, blank=False)
    donador = models.BooleanField(default=False, blank=False)