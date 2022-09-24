from unittest import TestCase

from django.urls import reverse


class PlatformUsersURLsTest(TestCase):
    def test_dashboard_url_path_is_correct(self):
        url = reverse('platform_users:dashboard_view')
        self.assertEqual(url, '/users/dashboard/')
