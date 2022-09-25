from django.shortcuts import render
from platform_users.models import Task


# Create your views here.
def home(request):
    tasks = Task.objects.filter(is_published=True).order_by('-created_at')[:10]
    return render(request, 'home/home.html', {'tasks': tasks})
