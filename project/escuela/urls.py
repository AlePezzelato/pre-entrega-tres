
from django.urls import path
from escuela.views import index

app_name = "escuela"

urlpatterns = [
    path("", index, name="index"),
]
