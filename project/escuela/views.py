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

def modificar_alumno(request, pk:int):
    consulta =modificar_alumno.objects.get(id=pk)
    if request.method == "POST":
        form = AlumnoForm(request.POST, instance=consulta)
        if form.is_valid():
            form.save()
            return redirect("escuela:listar_alumnos")
    else:
        form = AlumnoForm()
    return render(request, "escuela/modificar_alumno.html",{"form":form})

def eliminar_alumno(request, pk:int):
    consulta =eliminar_alumno.objects.get(id=pk)
    if request.method == "POST":
        consulta.delete()
        return redirect("escuela:listar_alumnos")
    return render (request, "escuela/confirma_eliminacion_alumno.html", {"object":consulta})
    