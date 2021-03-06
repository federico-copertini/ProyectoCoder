
from django.contrib import admin
from django.urls import path, include

from .views import *

urlpatterns = [

    #URLs de ProyectoCoderAPP
    path('', inicio, name = "inicio"),
    path('profesores/', profesores, name = "profesores"),
    path('estudiantes/', estudiantes, name = "estudiantes"),
    path('cursos/', cursos, name = "cursos"),
    path('crear_curso/', crear_curso, name = "crear_curso"),
    path('entregables/', entregables, name = "entregables"),
    path('buscar_comision/', buscar_comision, name = "Buscar_comision"),
    #path('base/', base),
]
