from django.urls import path
from . import views
app_name = 'demande_transport'
urlpatterns = [
    path('',views.demande, name='demande')
]


