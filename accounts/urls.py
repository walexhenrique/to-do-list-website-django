from django.urls import path

from accounts import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.login_view, name='login_view'),
    path('login/auth/', views.login_auth_view, name='login_auth_view'),
    path('logout/', views.logout_view, name='logout_view'),
]
