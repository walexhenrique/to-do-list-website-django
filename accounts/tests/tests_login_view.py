
from accounts import views
from accounts.forms.login_form import LoginForm
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import resolve, reverse


class LoginViewTest(TestCase):
    def test_view_login_returns_status_code_200(self):
        url = reverse('accounts:login_view')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/login.html')
    
    def test_view_login_shows_template_correct(self):
        url = reverse('accounts:login_view')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'accounts/login.html')

    def test_view_login_is_load_function_correct(self):
        """
        Checks if it is loading the correct view function for login
        """
        url = reverse('accounts:login_view')
        func_view = resolve(url)

        self.assertEqual(func_view.func, views.login_view)

    def test_view_login_load_form_in_content(self):
        url = reverse('accounts:login_view')
        response = self.client.get(url)

        self.assertIn('form', response.context)

    def test_view_login_checks_if_authentication_works(self):
        url = reverse('accounts:login_auth_view')
        User.objects.create_user(username='jumento', password='jumento2.0')
        response = self.client.post(url, data={'username':'jumento', 'password': 'jumento2.0'}, follow=True)
        self.assertRedirects(response, '/accounts/login/')

    def test_view_login_returns_404_if_request_method_is_not_POST(self):
        url = reverse('accounts:login_auth_view')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
    

        
