"""
URL configuration for monprojet4 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from exercice1 import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('reserva', views.reservation, name='reservation'),
    path('about', views.about, name='about'),
    path('menu', views.menu, name='menu'),
    path('special', views.special, name='special-dishes'),
    path('confirmation', views.confirmation, name='confirmation'),
    path('envoi', views.envoi, name='envoi'),
    path('team', views.recuperer, name='team'),
    path('rechercher/', views.rechercher, name='rechercher'),
    path('supprimer/<int:reserva_id>/', views.supprimer, name='supprimer'),
    path('modifier/<int:reserva_id>/', views.modifier, name='modifier'),
]   
   
