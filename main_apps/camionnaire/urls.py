from django.urls import path
from . import views
app_name = 'camionnaire'
urlpatterns = [
    path('',views.camionnaire, name='camionnaire')
]


