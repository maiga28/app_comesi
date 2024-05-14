from django.shortcuts import render
from django.test import SimpleTestCase, override_settings

def index(request):
    return render(request, 'index.html')

def custom_page_not_found(request, unknown_path):
    return render(request, '404.html', {'unknown_path': unknown_path}, status=404)