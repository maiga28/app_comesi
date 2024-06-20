from django.db import models
# from main_apps.gestion.models import *

class Camionneur(models.Model):
    STATUS_CHOICES = [
        ('actif', 'Actif'),
        ('inactif', 'Inactif'),
    ]

    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='media/', blank=True, null=True)
    background = models.ImageField(upload_to='media/', blank=True, null=True)
    date_de_naissance = models.DateField()
    adresse = models.CharField(max_length=255)
    numero_de_telephone = models.CharField(max_length=20)
    email = models.EmailField()
    numero_de_permis = models.CharField(max_length=50)
    experience = models.IntegerField()  # en années
    entreprise_employeur = models.CharField(max_length=100)
    type_de_camion_conduit = models.CharField(max_length=100)
    disponibilite = models.BooleanField(default=True)
    statut_d_emploi = models.CharField(max_length=10, choices=STATUS_CHOICES, default='actif')
    

    def __str__(self):
        return f"{self.nom} {self.prenom}"

class Camion(models.Model):
    STATUT_CHOICES = [
        ('en_service', 'En service'),
        ('en_reparation', 'En réparation'),
    ]

    id = models.AutoField(primary_key=True)
    modele = models.CharField(max_length=100)
    marque = models.CharField(max_length=100)
    annee = models.IntegerField()
    plaque_d_immatriculation = models.CharField(max_length=20)
    capacite_de_charge = models.FloatField()  # en tonnes par exemple
    statut = models.CharField(max_length=15, choices=STATUT_CHOICES, default='en_service')
    camionneur = models.ForeignKey(Camionneur, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.marque} {self.modele} ({self.plaque_d_immatriculation})"


