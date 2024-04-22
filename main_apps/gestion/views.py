from django.shortcuts import render

# Create your views here.
def gestion(request):
    return render(request,'gestion/gestion.html')

