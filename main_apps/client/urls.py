from django.urls import path
from . import views
app_name = 'client'
urlpatterns = [
    path('',views.client, name='client'),
    path('ajouter_client/',views.ajouter_client, name='ajouter_client'),
    path('list_client/',views.list_client, name='list_client'),
    path('delete_client/',views.delete_client, name='delete_client'),
    path('update_client/',views.update_client, name='update_client'),
]


