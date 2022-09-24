from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import Http404, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse

from accounts.forms.login_form import LoginForm
from accounts.forms.register_form import RegisterForm


# Create your views here.
def login_view(request):
    if request.user.is_authenticated:
        return redirect(reverse('platform_users:dashboard_view'))
        
    form = LoginForm()
    return render(request, 'accounts/login.html', {'form':form})

def login_auth_view(request):
    if request.method != 'POST':
        raise Http404()

    username = request.POST.get('username', '')
    password = request.POST.get('password', '')

    user = authenticate(request, username=username, password=password)

    if user:
        login(request, user)
        return redirect(reverse('platform_users:dashboard_view'))

    
    return redirect(reverse('accounts:login_view'))

def logout_view(request):
    logout(request)
    return redirect(reverse('accounts:login_view'))


def register_view(request):
    if request.user.is_authenticated:
        return redirect(reverse('platform_users:dashboard_view'))

    register_data = request.session.get('register_form_data')

    form = RegisterForm(register_data)
    return render(request, 'accounts/register.html', {'form': form})

def register_create_view(request):
    if request.method != 'POST':
        raise Http404()

    POST = request.POST
    request.session['register_form_data'] = POST

    form = RegisterForm(POST)
    if form.is_valid():
        user = form.save(commit=False)
        user.set_password(user.password)
        user.save()

        del(request.session['register_form_data'])
        return redirect(reverse('accounts:login_view'))
    
    return redirect(reverse('accounts:register_view'))
