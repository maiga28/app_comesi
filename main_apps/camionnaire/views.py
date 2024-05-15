from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.shortcuts import redirect
from main_apps.decorators import group_required

@receiver(user_logged_in)
def user_logged_in_callback(sender, request, user, **kwargs):
    if user.groups.filter(name='client').exists():
        if not request.path.startswith('client:client'):
            return redirect('client:client')
    elif user.groups.filter(name='admin').exists():
        if not request.path.startswith('/gestion/'):
            return redirect('gestion:gestion')
    elif user.groups.filter(name='Camionneurs').exists():
        if not request.path.startswith('/camionnaire/'):
            return redirect('camionnaire:camionnaire')

# Create your views here.

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from datetime import datetime
from django.contrib.auth.decorators import permission_required

@group_required('Camionneurs')
@login_required(login_url='/account_login/')
def camionnaire(request):

    
    now = datetime.now()
    if now.hour < 12:
        message = "Bonjour"
    else:
        message = "Bonsoir"
    context = {
        'message': message
    }
    return render(request, 'camionnaire/camionnaire.html', context)



@group_required('admin')
@login_required(login_url='/account_login/')
def list_camionnaire(request):
    return render(request, 'camionnaire/list_camionnaire.html')

@group_required('admin')
@login_required(login_url='/account_login/')
def ajouter_camionnaire(request):
    return render(request, 'camionnaire/aCamionneursjouter_camionnaire.html')

@group_required('admin')
@login_required(login_url='/account_login/')
def update_camionnaire(request):
    return render(request, 'camionnaire/update_camionnaire.html')

@group_required('admin')
@login_required(login_url='/account_login/')
def delete_camionnaire(request):
    return render(request, 'camionnaire/delete_camionnaire.html')

# def ajouter_camionnaire(request):
#     return render(request, 'camionnaire/ajouter_camionnaire.html')