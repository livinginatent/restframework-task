from django.test import SimpleTestCase
from django.urls import resolve, reverse
from barber.views import GetBarbers, GetBarber, CreateBarber, UpdateBarber


class TestUrls(SimpleTestCase):
    def test_barbers_url_resolves(self):
        url = reverse('barbers')
        self.assertEquals(resolve(url).func.__name__,
                          GetBarbers.as_view().__name__)

    def test_single_barber_url_resolves(self):
        url = reverse('barber', args=['pk'])
        self.assertEquals(resolve(url).func.__name__,
                          GetBarber.as_view().__name__)

    def test_create_barber_url_resolves(self):
        url = reverse('create-barber')
        self.assertEquals(resolve(url).func.__name__,
                          CreateBarber.as_view().__name__)

    def test_update_barber_url_resolves(self):
        url = reverse('update-barber', args=['pk'])
        self.assertEquals(resolve(url).func.__name__,
                          UpdateBarber.as_view().__name__)
