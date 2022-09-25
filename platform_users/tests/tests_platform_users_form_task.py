from django.test import TestCase
from platform_users.forms.form_task import TaskForm


class TaskFormTest(TestCase):
    def setUp(self) -> None:
        self.data = {
            'title': 'title',
            'desc': 'Desc',
            'is_published': True,
            'is_finished': True,
        }
        

    def test_title_longer_than_50_characteres_generates_msg_error(self):
        self.data['title'] = 'A'*51
        form = TaskForm(self.data)
        form.is_valid()

        self.assertIn('The text is too longer', form.errors.get('title'))

    def test_field_labels_name_is_correct(self):
        labels = [
            ('title', 'TITULO'),
            ('desc', 'DESCRICAO'),
            ('is_published', 'TAREFA PUBLICA'),
            ('is_finished', 'TAREFA FINALIZADA'),
        ]
        form = TaskForm(self.data)

        for field, label in labels:
            with self.subTest(field=field, label=label):
                self.assertEqual(form[field].label, label)
