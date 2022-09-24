from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse

from platform_users.models import Task


# Create your views here.
@login_required(login_url='accounts:login_view')
def dashboard(request):
    user = request.user
    print(user)
    tasks = Task.objects.filter(user=user)
    print(tasks)
    
    return render(request, 'platform_users/dashboard.html', {'tasks': tasks})
