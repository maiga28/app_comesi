from django.urls import path
from . import views
app_name = 'camionnaire'
urlpatterns = [
    path('',views.camionnaire, name='camionnaire'),
    path('list_camionnaire/',views.list_camionnaire, name='list_camionnaire'),
    path('ajouter_camionnaire/',views.ajouter_camionnaire, name='ajouter_camionnaire'),
]


