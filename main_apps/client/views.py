from django.shortcuts import render

# Create your views here.
def client(request):
    return render(request, 'client/client.html')