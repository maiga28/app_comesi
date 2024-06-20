from django.db import models

# Create your models here.
from main_apps.comionneur.models import *

class Company(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    unit_weight = models.FloatField()

    def __str__(self):
        return self.name

from django.db import models
from main_apps.comionneur.models import Camionneur # Import des modèles nécessaires

class Order(models.Model):
    order_number = models.CharField(max_length=50, unique=True)
    order_date = models.DateField()
    expected_delivery_date = models.DateField()
    expected_delivery_time_start = models.TimeField()
    expected_delivery_time_end = models.TimeField()
    loading_address = models.CharField(max_length=255)
    unloading_address = models.CharField(max_length=255)
    shipper = models.ForeignKey(Company, related_name='shipper_orders', on_delete=models.CASCADE)
    recipient = models.ForeignKey(Company, related_name='recipient_orders', on_delete=models.CASCADE)
    driver = models.ForeignKey(Camionneur, on_delete=models.CASCADE)
    special_instructions = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.order_number

class Livraison(models.Model):
    STATUT_CHOICES = [
        ('en_cours', 'En cours'),
        ('livree', 'Livrée'),
        ('annulee', 'Annulée'),
    ]

    id = models.AutoField(primary_key=True)
    camionneur = models.ForeignKey(Camionneur, on_delete=models.CASCADE, related_name='livraisons')
    date_de_la_livraison = models.DateField()
    adresse_de_depart = models.CharField(max_length=255)
    adresse_de_destination = models.CharField(max_length=255)
    type_de_marchandise = models.CharField(max_length=100)
    poids_de_la_marchandise = models.FloatField()  # en kilogrammes par exemple
    statut_de_la_livraison = models.CharField(max_length=10, choices=STATUT_CHOICES, default='en_cours')
    order = models.ForeignKey(Order, related_name='livraisons', on_delete=models.CASCADE)
    products = models.ManyToManyField('Product', through='LivraisonProduct', related_name='livraisons')

    def __str__(self):
        return f"Livraison {self.id} - {self.camionneur.nom} {self.camionneur.prenom}"

class LivraisonProduct(models.Model):
    livraison = models.ForeignKey(Livraison, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    @property
    def total_weight(self):
        return self.quantity * self.product.unit_weight

    def __str__(self):
        return f"{self.product.name} x {self.quantity} (Livraison: {self.livraison.id})"




class OrderProduct(models.Model):
    
    order = models.ForeignKey(Order, related_name='order_products', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    @property
    def total_weight(self):
        return self.quantity * self.product.unit_weight

    def __str__(self):
        return f"{self.product.name} x {self.quantity} (Order: {self.order.order_number})"
