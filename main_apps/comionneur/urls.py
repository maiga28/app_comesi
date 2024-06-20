from django.urls import path
from . import views

from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

app_name = 'camionnaire'

urlpatterns = [
    path('',views.camionneur, name='camionnaire'),
    path('list_camionnaire/',views.list_camionnaire, name='list_camionnaire'),
    path('detail_camionneur/<int:pk>/', views.detail_camionneur, name='detail_camionneur'),
    path('delete_camionnaire/',views.delete_camionnaire, name='delete_camionnaire'),
    path('update_camionnaire/',views.update_camionnaire, name='update_camionnaire'),
]


