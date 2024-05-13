from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from datetime import datetime
from main_apps.camionnaire.models import *
from main_apps.camionnaire.models import *
from main_apps.client.models import *
from main_apps.settings.models import *

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

@login_required
def gestion(request):
    users = User.objects.all()
    now = datetime.now()
    if now.hour < 12:
        message = "Bonjour"
    else:
        message = "Bonsoir"
    context = {
        'users': users,
        'message': message
    }
    return render(request, 'gestion/gestion.html', context)


