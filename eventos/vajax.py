from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate,logout
from django.contrib.auth import login as log
from django.contrib import auth

@csrf_exempt
def login(request):
    if (request.method == "POST"):
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        user = authenticate(request, username=email, password=password)

        if user is not None:
            log(request, user)
            request.session["user"] = user.id
            return HttpResponse("Exito")
        else:
            return HttpResponse("El usuario y/o password no coinciden")

    return HttpResponse("Metodo no valido")

@csrf_exempt
def cerrarSesion(request):

    logout(request)
    return HttpResponse("Exito")


@csrf_exempt
def registrar(request):
    if(request.method=="POST"):
        email=request.POST.get('email')
        password=request.POST.get('password')
        try:
            user=User.objects.create_user(email,email,password)
            user.save()
            return HttpResponse("Exito")

        except:
            return HttpResponse("Error al crear usuario")

    return HttpResponse("Metodo no valido")

@csrf_exempt
def eliminar(request):
    if(request.method=="POST"):
        try:
            ev=Event.objects.get(pk=request.POST.get("id"))
            ev.delete()
            return HttpResponse ("Exito")
        except Exception as e:
            print(str(e))
            return HttpResponse("Error al eliminar evento")


    return HttpResponse("Metodo no valido")

@csrf_exempt
def createEvent(request):
    if(request.method=="POST"):
        _name=request.POST.get('name')
        _userId=request.session["user"]
        _categoryId=request.POST.get('category')
        _place=request.POST.get('place')
        _address=request.POST.get('address')
        _start_date=request.POST.get('start_date')
        _finish_date=request.POST.get('finish_date')
        _typeId= request.POST.get('type')

        _user=User.objects.get(pk=_userId)
        _category=Category.objects.get(pk=_categoryId)
        _type=Type.objects.get(pk=_typeId)

        try:
            event=Event(person=_user, name=_name, category=_category, place=_place,address=_address, start_date=_start_date,finish_date=_finish_date, type=_type)
            event.save()
            return HttpResponse("Exito")

        except Exception as e:
            print(str(e))
            return HttpResponse("Error al crear evento")

    return HttpResponse("Metodo no valido")

@csrf_exempt
def modificarEvento(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        _categoryId = request.POST.get('category')
        place = request.POST.get('place')
        address =request.POST.get('address')
        start_date =request.POST.get('start_date')
        finish_date = request.POST.get('finish_date')
        _typeId =request.POST.get('type')
        _eventId = request.POST.get('id')

        category = Category.objects.get(pk=_categoryId)
        type = Type.objects.get(pk=_typeId)

        """
        ev=Event.objects.get(pk=_eventId)
        ev.name=name
        ev.category=category
        ev.place=place
        ev.address=address
        ev.start_date=start_date
        ev.finish_date=finish_date
        ev.type=type
        print("eventVajax: "+ _eventId)
        if(ev.save()):
            return HttpResponse("Exito")
        else:
            return HttpResponse("Error al modificar evento")

        """
        if (Event.objects.select_for_update().filter(id=_eventId).update(name=name, category=category, place=place,address=address, start_date=start_date,finish_date=finish_date, type=type)):
            return HttpResponse("Exito")
        else:
            return HttpResponse("Error al modificar evento")

    else:
        return HttpResponse('Metodo no definido')
