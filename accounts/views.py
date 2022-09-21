from django.shortcuts import HttpResponse, render


# Create your views here.
def login(request):
    return render(request, 'accounts/login.html')
