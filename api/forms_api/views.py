from django.shortcuts import render,redirect

from .forms import *
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from main_apps.comionneur.models import *
from django.shortcuts import render, redirect, get_object_or_404
from .forms import AjouterCamionneurForm
from django.contrib.auth.decorators import login_required
from django.utils.termcolors import background



# @login_required(login_url='/account_login/')
# def ajouter_camionneur(request):
#     if request.method == "POST":
#         form = AjouterCamionneurForm(request.POST)
#         if form.is_valid():
#             # Extract the cleaned data correctly
#             nom = form.cleaned_data['nom']
#             prenom = form.cleaned_data['prenom']
#             numero_de_telephone = form.cleaned_data['numero_de_telephone']
#             email = form.cleaned_data['email']
#             entreprise_employeur = form.cleaned_data['entreprise_employeur']
#             numero_de_permis = form.cleaned_data['numero_de_permis']
#             experience = form.cleaned_data['experience']
#             type_de_camion_conduit = form.cleaned_data['type_de_camion_conduit']
#             date_de_naissance = form.cleaned_data['date_de_naissance']
#             photo = form.cleaned_data['photo']
#             background = form.cleaned_data['background']
#             # Manually create a Camionneur instance and save it
#             camionneur = Camionneur.objects.create(
#                 nom=nom,
#                 prenom=prenom,
#                 numero_de_telephone=numero_de_telephone,
#                 email=email,
#                 entreprise_employeur=entreprise_employeur,
#                 numero_de_permis=numero_de_permis,
#                 experience=experience,
#                 type_de_camion_conduit=type_de_camion_conduit,
#                 date_de_naissance=date_de_naissance,
#                 photo=photo,
#                 background=background
#             )
#             camionneur.save()
            
#             return redirect('comionneur:lis_camionneur')
#     else:
#         form = AjouterCamionneurForm()

#     return render(request, 'camionneur/list_camionneur.html', {'form': form})



@login_required(login_url='/account_login/')
def update_camionneur(request, pk):
    camionneur = get_object_or_404(Camionneur, pk=pk)
    if request.method == "POST":
        form = UpdateCamionneurForm(request.POST, instance=camionneur)
        if form.is_valid():
            form.save()
            return redirect('gestion:gestion')
    else:
        form = UpdateCamionneurForm()
    return render(request, 'camionneur/update_camionneur.html', {'form': form})


@login_required(login_url='/account_login/')
def delete_camionneur(request, pk):
    camionneur = get_object_or_404(Camionneur, pk=pk)
    if request.method == "POST":
        camionneur.delete()
        return redirect('gestion:gestion')
    return render(request, 'camionneur/delete_camionneur.html', {'camionneur': camionneur})
