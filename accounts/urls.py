from django.urls import path

from accounts import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.login_view, name='login_view'),
    path('login/auth/', views.login_auth_view, name='login_auth_view'),
    path('logout/', views.logout_view, name='logout_view'),
    path('register/', views.register_view, name='register_view'),
    path('register/create/', views.register_create_view, name='register_create_view'),
]
