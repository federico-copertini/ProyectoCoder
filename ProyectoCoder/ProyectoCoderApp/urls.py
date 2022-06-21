
from django.contrib import admin
from django.urls import path, include

from .views import *

urlpatterns = [

    #URLs de ProyectoCoderAPP
    path('profesores/', profesores),
    path('estudiantes/', estudiantes),
    path('cursos', cursos)
    path('entregables/', entregables),
]
