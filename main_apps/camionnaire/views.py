from django.shortcuts import render
# Create your views here.

def camionnaire(request):
    return render(request, 'camionnaire/camionnaire.html')


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