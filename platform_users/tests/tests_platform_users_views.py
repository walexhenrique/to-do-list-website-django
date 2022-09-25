from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from platform_users.models import Task


class PlatformUsersViewsTest(TestCase):
    def create_user(
        self,
        username='user',
        first_name='first name',
        last_name='last name',
        email='user@email.com',
        password='123456'
    ):
        return User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password)

    def create_task(
        self,
        user,
        title='title',
        desc='Description',
        is_published=True,
        is_finished=True,
    ):
        return Task(user=user, title=title, desc=desc, is_published=is_published, is_finished=is_finished).save()
    
    def test_view_dashboard_use_5_as_default_if_limit_is_invalid(self):
        url = reverse('platform_users:dashboard_view')
        user = self.create_user()
        self.client.login(username='user', password='123456')
        for i in range(8):
            self.create_task(user)
            
        response = self.client.get(url, data={'limit':'a'})
        self.assertEqual(response.context['limit'], '5')
    
    def test_view_dashboard_redirect_if_not_logged(self):
        url = reverse('platform_users:dashboard_view')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_view_update_redirect_if_not_logged(self):
        url = reverse('platform_users:update_view', kwargs={'id': 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
    
    def test_view_update_returns_status_code_404_if_task_id_not_exists(self):
        url = reverse('platform_users:update_view', kwargs={'id': 1})
        user = self.create_user()
        self.client.login(username='user', password='123456')

        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_view_update_returns_status_code_200_if_everything_went_well(self):
        url = reverse('platform_users:update_view', kwargs={'id': 1})
        user = self.create_user()
        self.client.login(username='user', password='123456')
        self.create_task(user)
        
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

        # Test if form in context
        self.assertIn('title', response.context['form'].fields)

    def test_view_update_create_redirect_if_not_logged(self):
        url = reverse('platform_users:update_create_view', kwargs={'id': 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
    
    def test_view_update_create_returns_status_404_if_request_method_not_equals_POST(self):
        url = reverse('platform_users:update_create_view', kwargs={'id': 1})
        user = self.create_user()
        self.client.login(username='user', password='123456')
        self.create_task(user)
        
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_view_update_create_redirect_to_dashboard_if_form_is_valid(self):
        url = reverse('platform_users:update_create_view', kwargs={'id': 1})
        user = self.create_user()
        self.client.login(username='user', password='123456')
        self.create_task(user)
        
        response = self.client.post(url, data={
            'title': 'sleep', 'desc':'Working...', 'is_published': True, 'is_finished': True,
            }
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('platform_users:dashboard_view'))
    
    def test_view_update_create_redirect_to_update_view_if_form_is_not_valid(self):
        url = reverse('platform_users:update_create_view', kwargs={'id': 1})
        user = self.create_user()
        self.client.login(username='user', password='123456')
        self.create_task(user)
        
        response = self.client.post(url, data={
            'desc':'Working...', 'is_published': True, 'is_finished': True,
            }
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('platform_users:update_view', kwargs={'id':1}))

    def test_view_delete_redirect_if_not_logged(self):
        url = reverse('platform_users:delete_view', kwargs={'id': 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_view_delete_returns_status_code_404_if_task_id_not_exists(self):
        url = reverse('platform_users:delete_view', kwargs={'id': 1})
        user = self.create_user()
        self.client.login(username='user', password='123456')

        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_view_delete_returns_status_code_200_if_task_id_exists(self):
        url = reverse('platform_users:delete_view', kwargs={'id': 1})
        user = self.create_user()
        self.client.login(username='user', password='123456')
        self.create_task(user)

        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'platform_users/delete.html')

    def test_view_delete_confirm_redirect_if_not_logged(self):
        url = reverse('platform_users:delete_confirm_view', kwargs={'id': 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_view_delete_confirm_returns_status_404_if_request_method_not_equals_POST(self):
        url = reverse('platform_users:delete_confirm_view', kwargs={'id': 1})
        user = self.create_user()
        self.client.login(username='user', password='123456')
        self.create_task(user)
        
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
    
    def test_view_delete_confirm_delete_task_and_redirect_to_dashboard(self):
        url = reverse('platform_users:delete_confirm_view', kwargs={'id': 1})
        user = self.create_user()
        self.client.login(username='user', password='123456')
        self.create_task(user)
        
        response = self.client.post(url)
        task_exists = Task.objects.filter(id=1).exists()

        self.assertFalse(task_exists)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('platform_users:dashboard_view'))

    def test_view_register_task_redirect_if_not_logged(self):
        url = reverse('platform_users:register_task_view')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
    
    def test_view_register_task_returns_status_code_200_if_task_id_exists(self):
        url = reverse('platform_users:register_task_view')
        user = self.create_user()
        self.client.login(username='user', password='123456')

        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    
    def test_view_register_task_returns_status_404_if_request_method_not_equals_POST(self):
        url = reverse('platform_users:register_task_create')
        user = self.create_user()
        self.client.login(username='user', password='123456')
        self.create_task(user)
        
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_view_register_task_create_task_and_redirect_to_dashboard(self):
        url = reverse('platform_users:register_task_create')
        self.create_user()
        self.client.login(username='user', password='123456')
        
        response = self.client.post(url, data={
            'title': 'sleep', 'desc':'Working...', 'is_published': True, 'is_finished': True,
            }
        )
        task_exists = Task.objects.filter(id=1).exists()

        self.assertTrue(task_exists)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('platform_users:dashboard_view'))
    
    def test_view_register_task_create_redirect_to_update_view_if_form_is_not_valid(self):
        url = reverse('platform_users:register_task_create')
        self.create_user()
        self.client.login(username='user', password='123456')
        
        response = self.client.post(url, data={
            'desc':'Working...', 'is_published': True, 'is_finished': True,
            }
        )
        task_exists = Task.objects.filter(id=1).exists()

        self.assertFalse(task_exists)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('platform_users:register_task_view'))
    
