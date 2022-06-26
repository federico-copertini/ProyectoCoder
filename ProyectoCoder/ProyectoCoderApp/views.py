import datetime

from django.shortcuts import redirect, render
from django.http import HttpResponse
#from httplib2 import Http

from ProyectoCoderApp.models import *
from .forms import NuevoCurso

# Create your views here.

def inicio(request):

    nombre = "Juan"
    hoy = datetime.datetime.now()
    notas = [4,9,7,8,5,10]

    return render(request,"ProyectoCoderApp/index.html",{"mi_nombre":nombre,"dia_hora":hoy,"notas":notas})

def crear_curso(request):

    #post
    if request.method == "POST":
        info_formulario = request.POST
        
        curso = Curso(nombre=info_formulario["nombre"],comision=int(info_formulario["comision"]))
        
        curso.save()
        
        return redirect("cursos")
    
    #GET
    else:
        formulario_vacio = NuevoCurso()
        return render(request,"ProyectoCoderApp/formulario_curso.html",{"form":formulario_vacio})
   

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