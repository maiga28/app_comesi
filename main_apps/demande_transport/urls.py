from django.urls import path
from . import views

from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

app_name = 'demande_transport'

urlpatterns = [
    path('',views.demande, name='demande'),
    path('list_demande',views.list_demande, name='list_demande'),
    path('ajouter_demande',views.ajouter_demande, name='ajouter_demande'),
    path('update_demande',views.update_demande, name='update_demande'),
    path('delete_demande',views.delete_demande, name='delete_demande'),
]


