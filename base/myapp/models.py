from django.db import models

# Create your models here.
class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    correo = models.EmailField()
