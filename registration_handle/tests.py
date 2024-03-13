from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from profile_page.models import LeeriApprentices

class LeeriApprenticesTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.register_url = reverse('register')
        self.create_username_url = reverse('create_username')

    def test_submit_username_post(self):
        user = User.objects.create_user(username='testuser', email='test@example.com', password='password')
        self.client.login(username='testuser', password='password')

        response = self.client.post(reverse('submit_username'), {'username': 'test_username'})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(LeeriApprentices.objects.filter(username='test_username').exists())

    def test_submit_username_post_invalid(self):
        user = User.objects.create_user(username='testuser', email='test@example.com', password='password')
        self.client.login(username='testuser', password='password')

        response = self.client.post(reverse('submit_username'), {})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Please enter a username')

        LeeriApprentices.objects.create(username='existing_username', email='test@example.com', progress=0)
        response = self.client.post(reverse('submit_username'), {'username': 'existing_username'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Username is already taken')
