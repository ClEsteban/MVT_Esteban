from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context, loader

def familiares(request):
    return HttpResponse("Lista de Familiares")