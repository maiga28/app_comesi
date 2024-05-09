from django.shortcuts import render

# Create your views here.
def client(request):
    return render(request, 'client/client.html')

def list_client(request):
    return render(request, 'client/list_client.html')

def ajouter_client(request):
    return render(request,'client/ajouter_client.html')

def delete_client(request):
    return render(request,'client/delete_client.html')

def update_client(request):
    return render(request,'client/update_client.html')


