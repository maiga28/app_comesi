from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from datetime import datetime
from main_apps.camionnaire.models import *
from main_apps.camionnaire.models import *
from main_apps.client.models import *
from main_apps.settings.models import *

@login_required
def gestion(request):
    users = User.objects.all()
    now = datetime.now()
    if now.hour < 12:
        message = "Bonjour"
    else:
        message = "Bonsoir"
    context = {
        'users': users,
        'message': message
    }
    return render(request, 'gestion/gestion.html', context)


