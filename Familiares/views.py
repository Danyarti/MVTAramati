from django.shortcuts import render
from django.http import HttpResponse
from .models import Familia
from django.template import loader

# Create your views here.
def familiar (request):
    familiar1=Familia(nombre="Julio", apellido="Rodriguez", edad=65, nacimiento="1965-12-17")
    familiar2=Familia(nombre="Pedro", apellido="Sanchez", edad=25, nacimiento="1995-1-7")
    familiar3=Familia(nombre="Maria", apellido="Tapia", edad=44, nacimiento="1980-08-30")
    familiar1.save()
    familiar2.save()
    familiar3.save()
    
    dic={"n1":familiar1.nombre, "ape1":familiar1.apellido, "ed1":familiar1.edad, "nac1":familiar1.nacimiento,
    "n2":familiar2.nombre, "ape2":familiar2.apellido, "ed2":familiar2.edad, "nac2":familiar2.nacimiento,
    "n3":familiar3.nombre, "ape3":familiar3.apellido, "ed3":familiar3.edad, "nac3":familiar3.nacimiento}

    plantilla=loader.get_template('templates.html')

    documento=plantilla.render(dic)


    return HttpResponse (documento)