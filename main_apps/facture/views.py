from django.shortcuts import render
from django.contrib.auth.models import User
from datetime import datetime

from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.shortcuts import redirect
from main_apps.decorators import group_required
from django.contrib.auth.decorators import login_required


@receiver(user_logged_in)
def user_logged_in_callback(sender, request, user, **kwargs):
    if user.groups.filter(name='client').exists():
        return redirect('client:client')
    elif user.groups.filter(name='admin').exists():
        return redirect('gestion:gestion')
    elif user.groups.filter(name='Camionneurs').exists():
        return redirect('camionnaire:camionnaire')
    else:
        # Redirection par défaut pour les utilisateurs sans groupe spécifié
        return redirect('client:client')  # Vous devez définir cette vue

@group_required('admin', login_url='/account_login/')
@login_required(login_url='/account_login/')
def facture(request):
    
    now = datetime.now()
    if now.hour < 12:
        message = "Bonjour"
    else:
        message = "Bonsoir"
    
    context = {
        
        'message' : message
    }
    
    return render(request, 'facture/facture.html', context)
    
# Create your views here.
@group_required('admin', login_url='/account_login/')
@login_required(login_url='/account_login/')
def ajouter_facture(request):
    return render(request,'facture/ajouter_facture.html')

# Create your views here.
@group_required('admin', login_url='/account_login/')
@login_required(login_url='/account_login/')
def list_facture(request):
    return render(request,'facture/list_facture.html')

# Create your views here.
@group_required('admin', login_url='/account_login/')
@login_required(login_url='/account_login/')
def update_facture(request):
    return render(request,'facture/update_facture.html')

# Create your views here.
@group_required('admin', login_url='/account_login/')
@login_required(login_url='/account_login/')
def delete_facture(request):
    return render(request,'facture/delete_facture.html')
