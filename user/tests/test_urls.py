from django.test import SimpleTestCase
from django.urls import resolve, reverse
from user.views import GetUsers, GetUser, UpdateUser, CreateUser


class TestUrls(SimpleTestCase):
    def test_users_resolves(self):
        url = reverse('users')
        self.assertEquals(resolve(url).func.__name__,
                          GetUsers.as_view().__name__)

    def test_create_url_resolves(self):
        url = reverse('create-user')
        self.assertEquals(resolve(url).func.__name__,
                          CreateUser.as_view().__name__)

    def test_single_user_url_resolves(self):
        url = reverse('user', args=['pk'])
        self.assertEquals(resolve(url).func.__name__,
                          GetUser.as_view().__name__)

    def test_update_user_url_resolves(self):
        url = reverse('update-user', args=['pk'])
        self.assertEquals(resolve(url).func.__name__,
                          UpdateUser.as_view().__name__)
