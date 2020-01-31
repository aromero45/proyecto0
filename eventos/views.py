
from . import models
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
import json
from django.views.decorators.csrf import csrf_exempt




# Create your views here.

#Se define endpoint para home
def index(request):
    events=[]
    _userID=request.session.get("user",0)
    if(_userID == 0):
        sesion=False
    else:
        sesion=True
        events = models.Event.objects.filter(person__id=_userID).order_by("-creation_date")

    context={"sesion":sesion, "events":events}
    return render(request,"index.html",context)


@csrf_exempt
#Se define endpoint para registro de usuario
def register(request):

    context = {}
    return render(request, "registro.html", context)

#Se define endpoint para modificacion de evento
@csrf_exempt
def modifyEvent(request,id_ev):
    print("modifyEventId "+ id_ev)
    _event=models.Event.objects.get(pk=id_ev)
    print("eventView: " + str(_event))
    _categories=models.Category.objects.all()
    _type= models.Type.objects.all()
    context={"event":_event, 'categories':_categories, 'types':_type}
    return render(request, "modify.html", context)

#Se define endpoint para creacion de evento
@csrf_exempt
def createEvent(request):
    _categories = models.Category.objects.all()
    _type = models.Type.objects.all()
    context = {'categories':_categories, 'types':_type}
    return render(request, "createEvent.html", context)

@csrf_exempt
def eventDetails(request,id_ev):

    _event=models.Event.objects.get(pk=id_ev)
    context={"evento":_event}
    return render(request, "details.html", context)

