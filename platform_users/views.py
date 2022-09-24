from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from platform_users.models import Task

from .forms.form_task import TaskForm


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

@login_required(login_url='accounts:login_view')
def update_view(request, id):
    task = get_object_or_404(Task, id=id)

    data = {
        'title': task.title,
        'desc': task.desc,
        'is_published': task.is_published,
        'is_finished': task.is_finished,
    }
    form = TaskForm(data)
    return render(request, 'platform_users/update.html', {'form': form, 'id':id})


@login_required(login_url='accounts:login_view')
def update_create_view(request, id):
    if request.method != 'POST':
        raise Http404()
    
    task = Task.objects.get(id=id)
    form = TaskForm(request.POST, instance=task)
    
    if form.is_valid():
        form.save()
        return redirect(reverse('platform_users:dashboard_view'))

    return redirect(reverse('platform_users:update_view', kwargs={'id':id}))

@login_required(login_url='accounts:login_view')
def delete_view(request, id):
    task = Task.objects.get(id=id)
    return render(request, 'platform_users/delete.html', {'task':task})

@login_required(login_url='accounts:login_view')
def delete_confirm_view(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect(reverse('platform_users:dashboard_view'))
