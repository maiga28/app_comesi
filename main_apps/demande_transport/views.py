from django.shortcuts import render

# Create your views here.
def demande(request):
    return render(request,'demande/demande.html')

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



