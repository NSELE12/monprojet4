from django.shortcuts import render,redirect, get_object_or_404
from .models import *

# Create your views here.
def index(request):
    return render(request, 'exercice1/index.html')
def reservation(request):
    return render(request, 'exercice1/reservation.html')
def about(request):
    return render(request, 'exercice1/about.html')
def confirmation(request):
    return render(request, 'exercice1/confirmation.html')
    
def special(request):
    return render(request, 'exercice1/special-dishes.html')

def menu(request):
    return render(request, 'exercice1/menu.html')


#Définition de la fonction qui va récuperer dans la base de données
def envoi(request):
    if request.method =='POST':
       nom= request.POST.get('name')
       email= request.POST.get('email')
       telephone= request.POST.get('phoneNumber')
       date= request.POST.get('date')
       heure= request.POST.get('heure')
       nombre= request.POST.get('nombre')
       message= request.POST.get('message')

#Création de l'objet
       reservation=Reservation.objects.create(
        nom=nom,
        email=email,
        telephone=telephone,
        date=date,
        heure=heure,
        nombre=nombre,
        message=message,
       )
        
#Enregistrer dans la base de données
       reservation.save
       return redirect("confirmation")
    else:
        return redirect("reservation")

#La fonction qui permet de récupérer les éléments de la bd et afficher
def recuperer(request):
    recuperation=Reservation.objects.all()
    context={'recuperation':recuperation}
    return render(request, 'exercice1/team.html', context)

#definir la fonction supprimer qui permet de recuperrer l'element à supprimer à l'aide de son id 
def supprimer(request, reserva_id):
    reserva= get_object_or_404(Reservation, pk=reserva_id)
    if request.method == 'POST':
        reserva.delete()
        return redirect('team')
    return render(request, 'exercice1/supprimer.html', {'reserva':reserva})


#definir la fonction modifier qui permet de recuperrer l'element à modifier à l'aide de son id 
def modifier(request, reserva_id):
    reserva= get_object_or_404(Reservation, pk=reserva_id)
    if request.method == 'POST':
       reserva.nom= request.POST['name']
       reserva.email= request.POST['email']
       reserva.telephone= request.POST['phoneNumber']
       reserva.date= request.POST['date']
       reserva.heure= request.POST['heure']
       reserva.nombre= request.POST['nombre']
       reserva.message= request.POST['message']
       reserva.save()
       return redirect('team')
    return render(request, 'exercice1/modifier.html', {'reserva': reserva} )
    
# instructions pour la recherche de l'élément dans la bd
def rechercher(request):
    rechercher = Reservation.objects.all()
    search_query = request.GET.get('search_query', '')
    print(f'search_query: {search_query}')  # Add this line
    if search_query:
        rechercher = rechercher.filter(nom__icontains=search_query)  
    return render(request, 'exercice1/team.html', {'rechercher': rechercher, 'search_query': search_query})

