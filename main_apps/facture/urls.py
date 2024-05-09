from django.urls import path
from . import views
app_name = 'facture'
urlpatterns = [
    path('',views.facture, name='facture'),
    path('list_facture/',views.list_facture, name='list_facture'),
    path('ajouter_facture/',views.ajouter_facture, name='ajouter_facture'),
    path('update_facture/',views.update_facture, name='update_facture'),
    path('delete_facture/',views.delete_facture, name='delete_facture'),
]


