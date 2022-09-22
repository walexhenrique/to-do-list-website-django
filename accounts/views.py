from django.shortcuts import render

from accounts.forms.login_form import LoginForm


# Create your views here.
def login_view(request):
    form = LoginForm()
    return render(request, 'accounts/login.html', {'form':form})
