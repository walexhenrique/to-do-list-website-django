from unittest import TestCase

from django.urls import reverse


class PlatformUsersURLsTest(TestCase):
    def test_dashboard_url_path_is_correct(self):
        url = reverse('platform_users:dashboard_view')
        self.assertEqual(url, '/users/dashboard/')
    
    def test_register_url_path_is_correct(self):
        url = reverse('platform_users:register_task_view')
        self.assertEqual(url, '/users/register/')

    def test_register_task_create_url_path_is_correct(self):
        url = reverse('platform_users:register_task_create')
        self.assertEqual(url, '/users/register/task_create/')
