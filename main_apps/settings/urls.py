from django.urls import path
from . import views

from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

app_name = 'settings'

urlpatterns = [
    path('',views.settings, name='settings'),
    
]


