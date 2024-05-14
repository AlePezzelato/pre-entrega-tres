from django.shortcuts import render

def index(request):
    return render (request, "escuela/index.html")
