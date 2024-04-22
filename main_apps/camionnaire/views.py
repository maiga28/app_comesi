from django.shortcuts import render
# Create your views here.

def camionnaire(request):
    return render(request, 'camionnaire/camionnaire.html')


def list_camionnaire(request):
    return render(request, 'camionnaire/list_camionnaire.html')

def ajouter_camionnaire(request):
    return render(request, 'camionnaire/ajouter_camionnaire.html')