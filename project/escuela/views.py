from django.shortcuts import render, redirect
from escuela.models import Alumno
from escuela.forms import AlumnoForm

def index(request):
    return render (request, "escuela/index.html")

def listar_alumnos(request):
    consulta = Alumno.objects.all()
    contexto = {"Alumnos":consulta}
    return render(request, "escuela/listar_alumnos.html", contexto)

def crear_alumno(request):
    if request.method == "POST":
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("escuela:listar_alumnos")
    else:
        form = AlumnoForm()
    return render(request, "escuela/crear_alumno.html",{"form":form})

