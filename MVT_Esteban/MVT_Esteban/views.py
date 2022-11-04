from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context, loader

def familiares(request):
    hoy = datetime.now()
    lista = 
    return HttpResponse(f"<h1>Lista de Familiares</h1> Hoy es {hoy}")