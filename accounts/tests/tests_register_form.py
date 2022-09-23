from accounts.forms.register_form import RegisterForm
from django.test import TestCase


class RegisterFormTest(TestCase):
    def test_fields_label(self):
        fields_labels = [
            ('username', 'NOME DE USUARIO'),
            ('first_name', 'PRIMEIRO NOME'),
            ('last_name', 'SOBRENOME'),
            ('email', 'EMAIL'),
            ('password', 'SENHA'),
            ('password2', 'REPITA A SUA SENHA'),
        ]
        form = RegisterForm()
        for field, label_about in fields_labels:
            with self.subTest(field=field, label_about=label_about):
                self.assertEqual(form.fields[field].label, label_about)


