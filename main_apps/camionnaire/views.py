from django.shortcuts import render
from datetime import datetime

# Create your views here.

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


def list_camionnaire(request):
    return render(request, 'camionnaire/list_camionnaire.html')

def ajouter_camionnaire(request):
    return render(request, 'camionnaire/update_camionnaire.html')

def update_camionnaire(request):
    return render(request, 'camionnaire/ajouter_camionnaire.html')

def delete_camionnaire(request):
    return render(request, 'camionnaire/delete_camionnaire.html')

# def ajouter_camionnaire(request):
#     return render(request, 'camionnaire/ajouter_camionnaire.html')