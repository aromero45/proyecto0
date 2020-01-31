"""proyectoEventos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from eventos import views, vajax
from django.urls import path


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/', views.index),
    url(r'^register/', views.register),
    url(r'^registrar/', vajax.registrar),
    url(r'^eliminar/', vajax.eliminar),
    url(r'^loggear/', vajax.login),
    url(r'^logout/', vajax.cerrarSesion),
    path('update/<str:id_ev>', views.modifyEvent),
    path('details/<str:id_ev>', views.eventDetails),
    url(r'^editar/', vajax.modificarEvento),
    url(r'^create/', views.createEvent),
    url(r'^crear/', vajax.createEvent),

]
