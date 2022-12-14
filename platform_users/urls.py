from django.urls import path

from platform_users import views

app_name = 'platform_users'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard_view'),
    path('update/<int:id>/', views.update_view, name='update_view'),
    path('update/create/<int:id>/', views.update_create_view, name='update_create_view'),
    path('delete/<int:id>/', views.delete_view, name='delete_view'),
    path('delete/confirm/<int:id>/', views.delete_confirm_view, name='delete_confirm_view'),
    path('register/', views.register_task_view, name='register_task_view'),
    path('register/task_create/', views.register_task_create, name='register_task_create'),
]
