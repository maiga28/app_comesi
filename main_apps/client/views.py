from django.shortcuts import render
from datetime import datetime

from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.shortcuts import redirect

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
# Create your views here.
def client(request):
    now = datetime.now()
    if now.hour < 12:
        message = "Bonjour"
    else:
        message = "Bonsoir"
    context = {
        'message': message
    }
    return render(request, 'client/client.html', context)

def list_client(request):
    return render(request, 'client/list_client.html')

def ajouter_client(request):
    return render(request,'client/ajouter_client.html')

def delete_client(request):
    return render(request,'client/delete_client.html')

def update_client(request):
    return render(request,'client/update_client.html')


