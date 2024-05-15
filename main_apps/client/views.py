from django.shortcuts import render
from datetime import datetime

from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.shortcuts import redirect
from main_apps.decorators import group_required
from django.contrib.auth.decorators import login_required

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

@group_required('client')
@login_required(login_url='/account_login/')
def client(request):
    user = request.user  
    now = datetime.now()
    if now.hour < 12:
        message = "Bonjour"
    else:
        message = "Bonsoir"
    context = {
        'message': message,
        'user': user
    }
    return render(request, 'client/client.html', context)

@group_required('admin', login_url='/account_login/')
@login_required(login_url='/account_login/')
def list_client(request):
    return render(request, 'client/list_client.html')

@group_required('admin', login_url='/account_login/')
@login_required(login_url='/account_login/')
def ajouter_client(request):
    return render(request,'client/ajouter_client.html')


@group_required('admin', login_url='/account_login/')
@login_required(login_url='/account_login/')
def delete_client(request):
    return render(request,'client/delete_client.html')

@group_required('admin', login_url='/account_login/')
@login_required(login_url='/account_login/')
def update_client(request):
    return render(request,'client/update_client.html')


