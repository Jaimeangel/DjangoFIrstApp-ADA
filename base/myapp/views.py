from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Estudiante

# Create your views here.
def listar_estudiantes(request):
    # obtenemos todos los registros en nuestra base de datos de tipo Estudiante
    data = Estudiante.objects.all() 
    # en nuestra nueva lista tendremos una lista de diccionarios para poder mostrar los datos como json
    new_data = []
    for elem in data:
        new_data.append({'nombre': elem.nombre, 'edad': elem.edad, 'correo': elem.correo})
    return JsonResponse(new_data, safe=False)