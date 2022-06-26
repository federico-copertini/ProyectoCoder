import datetime

from django.shortcuts import render
from django.http import HttpResponse
#from httplib2 import Http

from ProyectoCoderApp.models import *

# Create your views here.

def inicio(request):

    nombre = "Juan"
    hoy = datetime.datetime.now()
    notas = [4,9,7,8,5,10]

    return render(request,"ProyectoCoderApp/index.html",{"mi_nombre":nombre,"dia_hora":hoy,"notas":notas})

def crear_curso(request):

   
    return render(request,"ProyectoCoderApp/formulario_curso.html",{})

def profesores(request):
    
    profesores = Profesor.objects.all()
    
    return render(request,"ProyectoCoderApp/profesores.html",{"profesores":profesores})
def estudiantes(request):

    estudiantes = Estudiante.objects.all()

    return render(request,"ProyectoCoderApp/estudiantes.html",{"estudiantes":estudiantes})

def cursos(request):

    cursos = Curso.objects.all()

    return render(request,"ProyectoCoderApp/Cursos.html",{"cursos":cursos})

def base(request):

    return render(request,"ProyectoCoderApp/base.html",{})

def entregables(request):

    return HttpResponse("vista de entregables")