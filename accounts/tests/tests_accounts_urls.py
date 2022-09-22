from unittest import TestCase

from django.urls import reverse


class AccountsURLsTest(TestCase):
    def test_login_url_path_is_correct(self):
        """
        This test verifies that the path points to the correct location
        """
        
        url = reverse('accounts:login_view')
        self.assertEqual(url, '/accounts/login/')
