from django.test import TestCase
from django.urls import reverse


# signup page tests
class SignupTests(TestCase):
    
    def setUp(self) -> None:
        self.username = 'testuser'
        self.email = 'testuser@blog.com'
        self.password = 'password'


    def test_signup_page_url(self):
        response = self.client.get("/accounts/signup/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='registration/signup.html')

    
    def test_signup_page_view_name(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='registration/signup.html')

    
    def test_signup_form(self):
        response = self.client.post(reverse('signup'), data={
            'username':self.username,
            'email':self.email,
            'password1':self.password,
            'password2':self.password
        })
        self.assertEqual(response.status_code, 200)