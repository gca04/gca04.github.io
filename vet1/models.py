from django.db import models

# Create your models here.
class Cliente(models.Model):
    idCliente = models.IntegerField(primary_key=True)
    Rut = models.IntegerField()
    Nom_ap = models.CharField(max_length=45)
    Telefono = models.IntegerField()
    email = models.CharField(max_length=45)

    def __str__(self):
        return self.Nom_ap

class Mascota(models.Model):
    idMas = models.AutoField(primary_key=True)
    NombreMascota = models.CharField(max_length=45)
    Animal = models.CharField(max_length=45)
    Raza = models.CharField(max_length=45)
    chip = models.IntegerField()
    idCliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.Animal} ({self.Raza})"
