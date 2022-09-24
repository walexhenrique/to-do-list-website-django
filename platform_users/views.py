from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render

from platform_users.models import Task


# Create your views here.
@login_required(login_url='accounts:login_view')
def dashboard(request):
    user = request.user
    
    tasks = Task.objects.filter(user=user)
    limits = ['5', '8', '10']

    limit = request.GET.get('limit', '5')
    if not limit in limits:
        limit = limits[0]

    paginator = Paginator(tasks, limit)

    page_number = request.GET.get('page', '1')
    
    page_obj = paginator.get_page(page_number)
    
    
    return render(request, 'platform_users/dashboard.html', {
        'tasks': page_obj,
        'quantity_per_page': limits,
        'limit': limit,
        })
