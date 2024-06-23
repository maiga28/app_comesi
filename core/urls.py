"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .views import index

from django.conf.urls import handler404
from .views import custom_page_not_found

from django.urls import path
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('gestion/', include('main_apps.gestion.urls')),
    path('client/', include('main_apps.client.urls')),
    path('facture/', include('main_apps.facture.urls')),
    path('demande/', include('main_apps.demande_transport.urls')),
    path('camionneur/', include('main_apps.comionneur.urls')),
    path('settings/', include('main_apps.settings.urls')),
    path('accounts/login/', auth_views.LoginView.as_view(), name='account_login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='account_logout'),
    path('account/', include('allauth.urls')),
    path('api/', include('api.forms_api.urls')),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    path('<path:unknown_path>', custom_page_not_found),
]



    

