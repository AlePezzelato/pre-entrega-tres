
from django.urls import path
from escuela.views import index, listar_alumnos

app_name = "escuela"

urlpatterns = [
    path("", index, name="index"),
    path("escuela/listar_alumnos", listar_alumnos, name="listar_alumnos")
]
