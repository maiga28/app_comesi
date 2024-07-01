from django.urls import path
from . import views

from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView


app_name = 'comionneur'


urlpatterns = [
    path('',views.camionneur, name='camionneur'),
    path('list_camionneur/',views.list_camionneur, name='list_camionneur'),
    path('detail_camionneur/<int:pk>/', views.detail_camionneur, name='detail_camionneur'),
    path('delete_camionneur/<int:pk>/',views.delete_camionneur, name='delete_camionneur'),
    path('update_camionneur/<int:pk>/',views.update_camionneur, name='update_camionneur'),
    path('search/', views.search_view, name='search'),
]


