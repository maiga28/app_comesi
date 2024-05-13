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
def demande(request):
    
    now = datetime.now()
    if now.hour < 12:
        message = "Bonjour"
    else:
        message = "Bonsoir"
    context = {
        'message': message
    }
    return render(request,'demande/demande.html', context)

# Create your views here.
def list_demande(request):
    return render(request,'demande/list_demande.html')

# Create your views here.
def ajouter_demande(request):
    return render(request,'demande/ajouter_demande.html')

# Create your views here.
def update_demande(request):
    return render(request,'demande/update_demande.html')

# Create your views here.
def delete_demande(request):
    return render(request,'demande/delete_demande.html')



