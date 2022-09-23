from accounts.views import register_view
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
        