from accounts.views import register_view
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import resolve, reverse


class RegisterViewTest(TestCase):
    
    def test_view_register_returns_status_code_200(self):
        url = reverse('accounts:register_view')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_view_register_shows_template_correct(self):
        url = reverse('accounts:register_view')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'accounts/register.html')

    def test_view_register_is_load_function_correct(self):
        url = reverse('accounts:register_view')
        func_view = resolve(url)
        self.assertEqual(func_view.func, register_view)
    
    def test_view_register_create_returns_error_404_if_method_not_equals_POST(self):
        url = reverse('accounts:register_create_view')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 404)
    
    def test_view_register_create_redirect_if_user_successfully_created(self):
        url = reverse('accounts:register_create_view')
        form_data = {
            'username': 'jorge',
            'first_name': 'jorgezito',
            'last_name': 'cabral',
            'email': 'jorge@cabral.com',
            'password': '123456',
            'password2': '123456',
        }
        
        response = self.client.post(url, data=form_data, follow=True)
        redirect_url = reverse('accounts:login_view')
        self.assertRedirects(response, redirect_url)

        # verify user created
        user = User.objects.filter(username=form_data['username']).exists()

        self.assertTrue(user)
        
    def test_view_register_create_redirect_to_register_if_invalid_form(self):
        url = reverse('accounts:register_create_view')
        form_data = {
            'username': 'jorge',
            'first_name': 'jorgezito',
            'last_name': 'cabral',
            'email': 'jorge@cabral.com',
            'password': '1234',
            'password2': '12345',
        }
        
        response = self.client.post(url, data=form_data, follow=True)
        redirect_url = reverse('accounts:register_view')
        self.assertRedirects(response, redirect_url)

        # User doesn't created
        user = User.objects.filter(username=form_data['username']).exists()

        self.assertFalse(user)
