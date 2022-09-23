from accounts.forms.register_form import RegisterForm
from django.test import TestCase
from django.urls import reverse


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
    
    def test_username_alredy_exists_in_bd(self):
        url = reverse('accounts:register_create_view')
        form_data = {
            'username': 'jorge',
            'first_name': 'jorgezito',
            'last_name': 'cabral',
            'email': 'jorge@cabral.com',
            'password': '123456',
            'password2': '123456',
        }
        user_exists_msg = 'Username alredy exists in database'
        # Create account and after try create another account with equals username
        
        self.client.post(url, data=form_data, follow=True)
        form_data['email'] = 'jorge1@cabral.com'

        response = self.client.post(url, data=form_data, follow=True)

        self.assertIn(user_exists_msg, response.context['form'].errors.get('username'))
        

        



