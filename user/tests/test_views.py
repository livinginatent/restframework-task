from django.test import TestCase, Client
from django.urls import reverse
from user.models import User


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.users_url = reverse('users')
        self.single_user_url = reverse('user', args=['1'])
        self.create_user_url = reverse('create-user')
        self.update_user_url = reverse('update-user', args=['1'])
        self.user1 = User.objects.create(
            first_name='test',
            last_name='test1',
            email='2@2.com',
            mobile='444'

        )

    def test_all_users_view(self):
        response = self.client.get(self.users_url)
        self.assertEquals(response.status_code, 200)

    def test_single_user_view(self):

        response = self.client.get(self.single_user_url)
        self.assertEquals(response.status_code, 200)

    def test_create_user_view(self):
        client = Client()
        response = client.get(self.create_user_url)
        self.assertEquals(response.status_code, 200)

    def test_update_user_view(self):
        client = Client()
        response = client.put(self.update_user_url)
        self.assertEquals(response.status_code, 200)
