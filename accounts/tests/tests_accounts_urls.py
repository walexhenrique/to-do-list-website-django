from unittest import TestCase

from django.urls import reverse


class AccountsURLsTest(TestCase):
    """
        This tests verifies that the path points to the correct location
     """
    def test_login_url_path_is_correct(self):
        url = reverse('accounts:login_view')
        self.assertEqual(url, '/accounts/login/')
    
    def test_login_auth_url_path_is_correct(self):
        url = reverse('accounts:login_auth_view')
        self.assertEqual(url, '/accounts/login/auth/')
    
    def test_logout_url_path_is_correct(self):
        url = reverse('accounts:logout_view')
        self.assertEqual(url, '/accounts/logout/')

    def test_register_url_path_is_correct(self):
        url = reverse('accounts:register_view')
        self.assertEqual(url, '/accounts/register/')
