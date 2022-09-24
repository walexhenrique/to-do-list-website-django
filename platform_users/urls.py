from django.urls import path

from platform_users import views

app_name = 'platform_users'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard_view'),
]
