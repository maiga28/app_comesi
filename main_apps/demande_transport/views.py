from django.shortcuts import render

# Create your views here.
def demande(request):
    return render(request,'demande/demande.html')