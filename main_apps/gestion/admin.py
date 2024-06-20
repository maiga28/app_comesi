from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone', 'email')
    search_fields = ('name', 'address', 'phone', 'email')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_number', 'order_date', 'expected_delivery_date', 'shipper', 'recipient', 'driver')
    search_fields = ('order_number', 'shipper__name', 'recipient__name', 'driver__name')

# @admin.register(Livraison)
# class LivraisonAdmin(admin.ModelAdmin):
#     list_display = ('id', 'camionneur', 'order', 'date_de_la_livraison', 'adresse_de_depart', 'adresse_de_destination', 'type_de_marchandise', 'poids_de_la_marchandise', 'statut_de_la_livraison')
#     search_fields = ('adresse_de_depart', 'adresse_de_destination', 'type_de_marchandise')
#     list_filter = ('statut_de_la_livraison', 'date_de_la_livraison')
#     fieldsets = (
#         (None, {
#             'fields': ('camionneur', 'date_de_la_livraison', 'adresse_de_depart', 'adresse_de_destination', 'type_de_marchandise', 'poids_de_la_marchandise', 'statut_de_la_livraison')
#         }),
#     )

@admin.register(Livraison)
class LivraisonAdmin(admin.ModelAdmin):
    list_display = ('id', 'camionneur', 'date_de_la_livraison', 'adresse_de_depart', 'adresse_de_destination', 'type_de_marchandise', 'poids_de_la_marchandise', 'statut_de_la_livraison', 'order')
    fields = ('camionneur', 'date_de_la_livraison', 'adresse_de_depart', 'adresse_de_destination', 'type_de_marchandise', 'poids_de_la_marchandise', 'statut_de_la_livraison', 'order')



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'unit_weight')
    search_fields = ('name',)

@admin.register(OrderProduct)
class OrderProductAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity', 'total_weight')
    search_fields = ('order__order_number', 'product__name')
    
@admin.register(LivraisonProduct)
class LivraisonProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'livraison', 'quantity', 'product')
    search_fields = ('id', 'product__name')
