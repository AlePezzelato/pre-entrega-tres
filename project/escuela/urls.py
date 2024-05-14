
from django.urls import path
from escuela.views import index, listar_alumnos, crear_alumno, modificar_alumno, eliminar_alumno

app_name = "escuela"

urlpatterns = [
    path("", index, name="index"),
    path("escuela/listar_alumnos", listar_alumnos, name="listar_alumnos"),
    path("escuela/crear_alumno", crear_alumno, name="crear_alumno"),
    path("escuela/modificar_alumno/<int:pk>", modificar_alumno, name="modificar_alumno"),
    path("escuela/eliminar_alumno/<int:pk>", eliminar_alumno, name="eliminar_alumno"),
]
