from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse


def saludar(request):
    return HttpResponse("Hola desde Django!")


def saludar2(request):
    return HttpResponse("<h1> Este es el título de la App </h1>")


def saludar3(request, nombre: str, apellido: str):
    nombre = nombre.capitalize()
    apellido = apellido.upper()
    return HttpResponse(f"{apellido}, {nombre}")


def index(request):
    ahora = datetime.now()
    contexto = {"fecha": ahora}
    return render(request, "core/index.html", contexto)
