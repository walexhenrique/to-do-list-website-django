from turtle import title

from django.test import TestCase
from platform_users.models import Task


class TaskModelTest(TestCase):
    def test_str_returns_attr_name(self):
        task = Task(title='title', desc='desc', is_published=True, is_finished=True)
        
        self.assertEqual(str(task), 'title')
