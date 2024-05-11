from django.shortcuts import render
from datetime import datetime
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


