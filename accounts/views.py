from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import Http404, HttpResponse
from django.shortcuts import redirect, render

from accounts.forms.login_form import LoginForm


# Create your views here.
def login_view(request):
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
        return redirect('accounts:login_view')

    
    return HttpResponse('asad')

def logout_view(request):
    logout(request)
