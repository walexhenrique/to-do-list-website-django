from accounts.forms.login_form import LoginForm
from django.test import SimpleTestCase


class LoginTestForm(SimpleTestCase):

    def test_login_form_valid_data(self):
        form = LoginForm(data={
            'username': 'user',
            'password': 'password'
        })

        self.assertTrue(form.is_valid())

    def test_login_form_no_data(self):
        form = LoginForm(data={})

        self.assertFalse(form.is_valid())
    
    def test_login_label_is_USERNAME_and_SENHA(self):
        form = LoginForm(data={
            'username':'user',
            'password':'password'
        })

        self.assertEqual(form['username'].field.label, 'USERNAME')
        self.assertEqual(form['password'].field.label, 'SENHA')
