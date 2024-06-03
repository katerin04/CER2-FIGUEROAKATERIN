from django.shortcuts import render, redirect
from .models import Proyecto, Profesor
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import Proyecto


def home(request):
    title = "Inicio"

    data = {
        "title" : title,
    }

    return render(request, 'core/home.html',data)


def docentes(request):
    title = "Profesores"

    data = {
        "title":title,
    }
    return render(request, 'core/docentes.html',data)



def guardar_proyecto(request):
    if request.method == 'POST':
        nuevo_proyecto = request.POST['nuevo_proyecto']
        alumno = request.POST['alumno']
        tema = request.POST['tema']
        profesor = request.POST['profesor']
        proyecto = Proyecto(nuevo_proyecto=nuevo_proyecto, alumno=alumno, tema=tema, profesor=profesor)
        proyecto.save()
        return HttpResponse('Proyecto guardado exitosamente!')
    else:
        return HttpResponse('Ha ocurrido un error al guardar el proyecto.')