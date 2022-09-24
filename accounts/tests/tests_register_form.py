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
    
    def test_email_alredy_exists_in_bd(self):
        url = reverse('accounts:register_create_view')
        form_data = {
            'username': 'jorge',
            'first_name': 'jorgezito',
            'last_name': 'cabral',
            'email': 'jorge@cabral.com',
            'password': '123456',
            'password2': '123456',
        }
        email_exists_msg = 'Email alredy exists in database'

        self.client.post(url, data=form_data, follow=True)
        form_data['username'] = 'batista'
        response = self.client.post(url, data=form_data, follow=True)

        self.assertIn(email_exists_msg, response.context['form'].errors.get('email'))

    def test_password_least_4_letters_not_valide(self):
        url = reverse('accounts:register_create_view')

        form_data = {
            'username': 'jorge',
            'first_name': 'jorgezito',
            'last_name': 'cabral',
            'email': 'jorge@cabral.com',
            'password': '123',
            'password2': '123',
        }

        password_is_short_msg = 'Error, Password is too short'

        response = self.client.post(url, data=form_data, follow=True)

        self.assertIn(password_is_short_msg, response.context['form'].errors.get('password'))
        
    def test_password2_least_4_letters_not_valide(self):
        url = reverse('accounts:register_create_view')

        form_data = {
            'username': 'jorge',
            'first_name': 'jorgezito',
            'last_name': 'cabral',
            'email': 'jorge@cabral.com',
            'password': '1234',
            'password2': '123',
        }

        password2_is_short_msg = 'Error, Password is too short'
        response = self.client.post(url, data=form_data, follow=True)

        self.assertIn(password2_is_short_msg, response.context['form'].errors.get('password2'))

    def test_password_and_password2_not_equals(self):
        url = reverse('accounts:register_create_view')

        form_data = {
            'username': 'jorge',
            'first_name': 'jorgezito',
            'last_name': 'cabral',
            'email': 'jorge@cabral.com',
            'password': '12345',
            'password2': '1234',
        }

        password_and_password2_not_equals_msg = 'Error, Passwords not equals'
        response = self.client.post(url, data=form_data, follow=True)
        self.assertIn(password_and_password2_not_equals_msg, response.context['form'].errors.get('__all__'))
        
    def test_register_user_valid_works_for_create_new_user_in_db(self):
        form_data = {
            'username': 'jorge',
            'first_name': 'jorgezito',
            'last_name': 'cabral',
            'email': 'jorge@cabral.com',
            'password': '12345',
            'password2': '12345',
        }
        form = RegisterForm(form_data)
        user = form.save(commit=False)
        user.set_password(user.password)
        user.save()

        user_exists = self.client.login(username='jorge', password='12345')
        self.assertTrue(user_exists)
