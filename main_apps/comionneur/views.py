from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.shortcuts import get_object_or_404, redirect
from main_apps.decorators import group_required
from main_apps.comionneur.models import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from datetime import datetime
from django.contrib.auth.decorators import permission_required
from api.forms_api.forms import *


@receiver(user_logged_in)
def user_logged_in_callback(sender, request, user, **kwargs):
    if user.groups.filter(name='client').exists():
        if not request.path.startswith('client:client'):
            return redirect('client:client')
    elif user.groups.filter(name='admin').exists():
        if not request.path.startswith('/gestion/'):
            return redirect('gestion:gestion')
    elif user.groups.filter(name='Camionneurs').exists():
        if not request.path.startswith('/camionneur/'):
            return redirect('camionneur:camionneur')

# Create your views here.



@group_required('Camionneurs','admin')
@login_required(login_url='/account_login/')
def camionneur(request):
    
    Total_camionneurs = Camionneur.objects.count()
    camionneurs = Camionneur.objects.all()
    
    now = datetime.now()
    if now.hour < 12:
        message = "Bonjour" 
    else:
        message = "Bonsoir"
        
    context = {
        'message': message,
        'camionneurs': camionneurs,
        'Total_camionneurs':Total_camionneurs
    }
    return render(request, 'camionneur/camionneur.html', context)



@group_required('admin')
@login_required(login_url='/account_login/')
def list_camionnaire(request):
    camionneurs = Camionneur.objects.all()
    
    context = {
        'camionneurs': camionneurs
    }
    return render(request, 'camionneur/list_camionneur.html', context)

@group_required('admin')
@login_required(login_url='/account_login/')
def detail_camionneur(request,pk):
    camionneurs = get_object_or_404(Camionneur, id=pk)
    # context = {
    #     'camionneurs':camionneurs
    # }
    return render(request, 'camionneur/detail_camionneur.html', {'camionneurs':camionneurs})

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