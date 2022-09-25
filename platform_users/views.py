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

@login_required(login_url='accounts:login_view')
def register_task_view(request):
    data = request.session.get('register_task_create')
    form = TaskForm(data)
    return render(request, 'platform_users/register_task.html', {'form':form})

@login_required(login_url='accounts:login_view')
def register_task_create(request):
    if request.method != 'POST':
        raise Http404()
    POST = request.POST
    request.session['register_task_create'] = POST
    
    form = TaskForm(POST)
    if form.is_valid():
        form_with_user = form.save(commit=False)
        form_with_user.user = request.user
        form_with_user.save()
        del(request.session['register_task_create'])
        return redirect(reverse('platform_users:dashboard_view'))
    
    return redirect(reverse('register_task_view'))
    