from django.http import HttpResponse
import datetime
from django.template import Template, Context
# from django.template import loader 
from django.template.loader import get_template
from django.shortcuts import render

# Nota de teoría: toda función definida
# en views.py se llama vista

## Primer clase

class Persona(object):

    def __init__(self, nombre, apellido):
        self.nombre = nombre

        self.apellido = apellido

def saludo(request): # primera vista

    p1 = Persona("Profesor Alberto", "Candelario")

    # nombre = "Juan"

    # apellido = "Pérez"

    temas_curso = ["Plantillas", "Modelos", "Formularios", "Vistas"]

    # temas_curso = []

    ahora = datetime.datetime.now()

    # VERSION ARCAICA PARA CARGAR PLANTILLAS 
    # doc_externo = open("C:/Users/alberto.candelario/Documents/proyecto_django_prueba/proyecto_alfa/proyecto_alfa/plantillas/miplantilla.html")
    # plt = Template(doc_externo.read())
    # doc_externo.close()

    # VERSION CORRECTA: USO DE "LOADERS"
    # Señalar a django donde se encuentran las plantillas

    # El nuevo template no es igual que el Template anterior
    # doc_externo = loader.get_template('miplantilla.html')
    # doc_externo = get_template('miplantilla.html')

    # ctx = Context({"nombre_persona": p1.nombre, 
    #                 "apellido_persona": p1.apellido, 
    #                 "momento_actual": ahora, 
    #                 "temas": temas_curso})

    # Puedes pasar el diccionario directamente al método render

    # documento = doc_externo.render({"nombre_persona": p1.nombre,
    #                                 "apellido_persona": p1.apellido, 
    #                                 "momento_actual": ahora, 
    #                                 "temas": temas_curso})

    # return HttpResponse(documento)

    return render(request, "miplantilla.html", {"nombre_persona": p1.nombre, 
                                                "apellido_persona": p1.apellido,  
                                                "momento_actual": ahora, 
                                                "temas": temas_curso})


def servicios(request):

    fecha_actual = datetime.datetime.now()

    return render(request,
                  "servicios.html",
                  {"dameFecha": fecha_actual})


def experiencia(request):

    return render(request,
                  "experiencia.html")


def despedida(request):
    return HttpResponse("¡Adiós, mundo!")

# Agregar contenido dinamico

# Puedes definir características al estilo html

def dameFecha(request):
    fecha_actual = datetime.datetime.now()
    documento = """<html>
    <body>
    <h1>
    Fecha y hora actuales %s
    </h1>
    </body>
    </html>""" % fecha_actual

    return HttpResponse(documento)

def calculaEdad(request, edad, year):
    
    # edadActual = 30
    periodo = year - 2025
    edadFutura = edad + periodo
    documento = """<html>
    <body>
    <h2>
    En el año %s tendrás %s años
    </h2>
    </body>
    </html>""" % (year, edadFutura)

    return HttpResponse(documento)