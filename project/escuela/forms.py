from django import forms
from . import models

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = models.Alumno
        fields = ["nombre", "apellido", "fecha_de_nacimiento", "docente_id", "materia_id"]