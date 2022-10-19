from django.test import TestCase, Client
from django.urls import reverse
from barber.models import Barber


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.barbers_url = reverse('barbers')
        self.single_barber_url = reverse('barber', args=['1'])
        self.create_barber_url = reverse('create-barber')
        self.update_barber_url = reverse('update-barber', args=['1'])
        self.barber1 = Barber.objects.create(
            name='test',
            address='london',
            phone='444'
        )

    def test_all_barbers_view(self):
        response = self.client.get(self.barbers_url)
        self.assertEquals(response.status_code, 200)

    def test_single_barber_view(self):

        response = self.client.get(self.single_barber_url)
        self.assertEquals(response.status_code, 200)

    def test_create_barber_view(self):
        client = Client()
        response = client.get(self.create_barber_url)
        self.assertEquals(response.status_code, 200)

    def test_update_barber_view(self):
        client = Client()
        response = client.put(self.update_barber_url)
        self.assertEquals(response.status_code, 200)
