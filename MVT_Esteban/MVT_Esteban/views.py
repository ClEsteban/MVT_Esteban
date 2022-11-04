from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context, loader

def familiares(request):
    archivo = open("./templates/plantilla_MVT.html")
    plantilla = Template(archivo.read())
    archivo.close()

    contexto = Context()

    pass

def fecha(request):

    hoy = datetime.now()
    lista = "db.sqlite3"
    return HttpResponse(f"<h1>Lista de Familiares</h1> Hoy es {hoy}")