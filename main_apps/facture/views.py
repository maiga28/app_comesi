from django.shortcuts import render
from django.contrib.auth.models import User
from datetime import datetime
# Create your views here.
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
def ajouter_facture(request):
    return render(request,'facture/ajouter_facture.html')

# Create your views here.
def list_facture(request):
    return render(request,'facture/list_facture.html')

# Create your views here.
def update_facture(request):
    return render(request,'facture/update_facture.html')

# Create your views here.
def delete_facture(request):
    return render(request,'facture/delete_facture.html')
