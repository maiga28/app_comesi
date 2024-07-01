from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect
from main_apps.decorators import group_required
from main_apps.comionneur.models import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from datetime import datetime
from django.contrib.auth.decorators import permission_required
from api.forms_api.forms import *
from django.db import IntegrityError
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.contrib import messages



# from django.db import IntegrityError
# from django.http import JsonResponse


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
def list_camionneur(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        data = {'message': 'Bonjour de Django!'}
        return JsonResponse(data)
    
    camionneurs = Camionneur.objects.all()
    paginator = Paginator(camionneurs, 8)  # 10 camionneurs par page

    # page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)
    # paginator = Paginator(proprietaires, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number) 
    if request.method == "POST":
        form = AjouterCamionneurForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, "Le camionneur a été ajouté avec succès.")
                return redirect('comionneur:list_camionneur')  # Redirige vers une page de succès
            except IntegrityError:
                form.add_error('username', "Ce nom d'utilisateur existe déjà. Veuillez en choisir un autre.")
        else:
            # Si le formulaire n'est pas valide, récupérez les données nettoyées pour les afficher
            nom = form.cleaned_data.get('nom', '')
            prenom = form.cleaned_data.get('prenom', '')
            numero_de_telephone = form.cleaned_data.get('numero_de_telephone', '')
            email = form.cleaned_data.get('email', '')
            entreprise_employeur = form.cleaned_data.get('entreprise_employeur', '')
            numero_de_permis = form.cleaned_data.get('numero_de_permis', '')
            experience = form.cleaned_data.get('experience', '')
            type_de_camion_conduit = form.cleaned_data.get('type_de_camion_conduit', '')
            date_de_naissance = form.cleaned_data.get('date_de_naissance', '')
            photo = form.cleaned_data.get('photo', None)
            background = form.cleaned_data.get('background', None)
    else:
        form = AjouterCamionneurForm()
    
    
    context = {
        'form': form,
        'camionneurs': camionneurs,
        'camionneurs': page_obj,
        'page_obj': page_obj
    }
    # data = {'message': 'Bonjour de Django!'}
    
    return render(request, 'camionneur/list_camionneur.html', context)



@login_required(login_url='/account_login/')
@group_required('admin')
def detail_camionneur(request, pk):
    camionneurs = get_object_or_404(Camionneur, id=pk)
    context = {
        'camionneurs': camionneurs
    }
    return render(request, 'camionneur/detail_camionneur.html', context)

@login_required(login_url='/account_login/')
@group_required('admin')
def update_camionneur(request,pk):
    camionneur = get_object_or_404(Camionneur, id=pk)
    if request.method == "POST":
        form = UpdateCamionneurForm(request.POST, request.FILES, instance=camionneur)
        if form.is_valid():
            form.save()
            return redirect('comionneur:list_camionneur')
    else:
        form = UpdateCamionneurForm(instance=camionneur)
    context = {
        'form': form,
        'camionneur': camionneur
    }
    return render(request, 'camionneur/update_camionneur.html', context)

@login_required(login_url='/account_login/')
@group_required('admin')
def delete_camionneur(request, pk):
    camionneurs = get_object_or_404(Camionneur, id=pk)
    if request.method == 'POST':
        camionneurs.delete()
        return redirect('comionneur:list_camionneur')
    context = {
        'camionneurs':camionneurs
    }
    return render(request, 'camionneur/delete_camionneur.html', context)

from django.shortcuts import render
from django.db.models import Q
from .models import Camionneur  # Assurez-vous d'importer le modèle approprié

def search_view(request):
    query = request.GET.get('q')
    results = []
    
    if query:
        results = Camionneur.objects.filter(
            Q(nom__icontains=query) | 
            Q(prenom__icontains=query) | 
            Q(entreprise_employeur__icontains=query) |
            Q(type_de_camion_conduit__icontains=query)
        )
    
    context = {
        'results': results,
        'query': query,
    }
    return render(request, 'camionneur/search_results.html', context)


# def ajouter_camionnaire(request):
#     return render(request, 'camionnaire/ajouter_camionnaire.html')