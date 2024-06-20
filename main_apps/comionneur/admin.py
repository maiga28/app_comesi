from django.contrib import admin
from .models import Camionneur, Camion
@admin.register(Camionneur)
class CamionneurAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'numero_de_telephone', 'email', 'entreprise_employeur', 'statut_d_emploi')
    search_fields = ('nom', 'prenom', 'numero_de_telephone', 'email', 'entreprise_employeur')
    list_filter = ('statut_d_emploi', 'entreprise_employeur')
    fieldsets = (
        (None, {
            'fields': ('nom', 'prenom', 'date_de_naissance', 'adresse', 'photo','background','numero_de_telephone', 'email')
        }),
        ('Détails professionnels', {
            'fields': ('numero_de_permis', 'experience', 'entreprise_employeur', 'type_de_camion_conduit', 'disponibilite', 'statut_d_emploi')
        }),
    )

@admin.register(Camion)
class CamionAdmin(admin.ModelAdmin):
    list_display = ('marque', 'modele', 'plaque_d_immatriculation', 'capacite_de_charge', 'statut', 'camionneur')
    search_fields = ('marque', 'modele', 'plaque_d_immatriculation')
    list_filter = ('statut',)
    fieldsets = (
        (None, {
            'fields': ('marque', 'modele', 'annee', 'plaque_d_immatriculation', 'capacite_de_charge', 'statut', 'camionneur')
        }),
    )

