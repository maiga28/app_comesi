from django.urls import path
from . import views
app_name = 'facture'
urlpatterns = [
    path('',views.facture, name='facture')
]


