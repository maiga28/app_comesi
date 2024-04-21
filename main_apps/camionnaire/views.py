from django.shortcuts import render
# Create your views here.

def camionnaire(request):
    return render(request, 'camionnaire/camionnaire.html')