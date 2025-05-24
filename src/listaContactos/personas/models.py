from django.db import models

# Create your models here.
class Persona(models.Model):
    nombres = models.CharField()
    apellidos = models.CharField()
    edad = models.IntegerField()