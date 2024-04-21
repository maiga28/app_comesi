from django.shortcuts import render

# Create your views here.
def facture(request):
    return render(request, 'facture/facture.html')
    