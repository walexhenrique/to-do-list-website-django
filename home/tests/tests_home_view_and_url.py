import time

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import resolve, reverse
from home.views import home
from platform_users.models import Task


class HomeViewAndURLsTest(TestCase):

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

    def setUp(self) -> None:
        self.url = reverse('home:home')

    def test_home_url_path_is_correct(self):
        self.assertEqual(self.url, '/')
    
    def test_home_loads_func_correct(self):
        func_view = resolve(self.url)
        self.assertEqual(func_view.func, home)
    
    def test_home_shows_template_correct(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'home/home.html')

    def test_home_shows_10_latest_tasks_published_in_template(self):
        user = self.create_user()
        for i in range(10):
            self.create_task(user)
            # time between tasks
            time.sleep(.5)
            
        
        response = self.client.get(self.url)
        self.assertEqual(len(response.context['tasks']), 10)
        # order_by -created_at
        self.assertTrue(response.context['tasks'][0].created_at > response.context['tasks'][8].created_at)

        