from django.shortcuts import render

# Create your views here.
def facture(request):
    return render(request, 'facture/facture.html')
    
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
