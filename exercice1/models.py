from django.db import models

# Create your models here.
class Reservation(models.Model):
    nom=models.CharField(max_length=30)
    email=models.EmailField()
    telephone=models.IntegerField()
    date=models.DateField()
    heure=models.TimeField()
    nombre=models.IntegerField()
    message=models.CharField(max_length=150)
    def __str__(self):
        return self.nom
    

