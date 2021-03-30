from django.db import models

# Create your models here.
class admin(models.Model):
    id=models.CharField(primary_key = True,max_length=10)
    nombre=models.CharField(max_length=40) 
    apellido=models.CharField(max_length=40)
    telefono=models.CharField(max_length=10)
    cedula=models.CharField(max_length=12)

    
class vehiculo(models.Model):
    destino=models.CharField(max_length=40)
    placa=models.CharField(max_length=10)
    numero_interno=models.CharField(max_length=10)
    pasajeros_de_viaje= models.CharField(max_length=200)
    cedula_de_pasajeros= models.CharField(max_length=200)



       