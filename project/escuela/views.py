from django.shortcuts import render
from escuela.models import Alumno

def index(request):
    return render (request, "escuela/index.html")

def listar_alumnos(request):
    consulta = Alumno.objects.all()
    contexto = {"Alumnos":consulta}
    return render(request, "escuela/listar_alumnos.html", contexto)
