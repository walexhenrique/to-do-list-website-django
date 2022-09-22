from accounts.views import logout_view
from django.contrib.auth import get_user
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import resolve, reverse


class LogoutViewTest(TestCase):
    def test_logout_view_is_load_correct_view(self):
        url = reverse('accounts:logout_view')
        func_view = resolve(url)
        self.assertEqual(func_view.func, logout_view)

    def test_logout_view_work_and_redirect_correct(self):
        url = reverse('accounts:logout_view')
        User.objects.create_user(username='joaquim', password="batata123")
        self.client.login(username='joaquim', password='batata123')

        response = self.client.get(url)
        url_redirect = reverse('accounts:login_view')
        self.assertRedirects(response, url_redirect)
                
        
