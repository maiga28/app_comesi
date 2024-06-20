from django.urls import path,include
from . import views



app_name = 'gestion'

urlpatterns = [
    
    path('', views.gestion, name='gestion'),
    
]


