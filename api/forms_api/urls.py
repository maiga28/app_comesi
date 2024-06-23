from django.urls import path
from . import views

app_name = 'forms_api'

urlpatterns = [
    
    # path('ajouter_camionneur/', views.ajouter_camionneur, name='ajouter_camionneur'),
    path('update_camionneur/<int:pk>/', views.update_camionneur, name='update_camionneur'),
    path('delete_camionneur/', views.delete_camionneur, name='delete_camionneur'),
    
]