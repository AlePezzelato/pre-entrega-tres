from django.db import models

class Materia(models.Model):
    nombre = models.CharField(max_length=150, unique=True)
    codigo = models.CharField(max_length=30, unique=True)
    
    def __str__(self) -> str:
        return self.nombre
    
class Docente(models.Model):
    nombre = models.CharField(max_length=150)
    apellido = models.CharField(max_length=150)
    materia_id = models.ForeignKey(Materia, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self) -> str:
        return f"{self.apellido}, {self.nombre}"


class Alumno(models.Model):
    nombre = models.CharField(max_length=150)
    apellido = models.CharField(max_length=150)
    fecha_de_nacimiento = models.DateField(null=True, blank=True)
    docente_id = models.ForeignKey(Docente, on_delete=models.SET_NULL, null=True)
    materia_id = models.ForeignKey(Materia, on_delete=models.SET_NULL, null=True)
    
    def __str__(self) -> str:
        return f"{self.apellido}, {self.nombre}"
    
    
