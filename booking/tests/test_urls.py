from django.test import SimpleTestCase
from django.urls import resolve, reverse
from booking.views import GetBookings, GetBooking, GetBarberBooking, GetUserBooking, CreateBooking, UpdateBooking


class TestUrls(SimpleTestCase):
    def test_bookings_url_resolves(self):
        url = reverse('bookings')
        self.assertEquals(resolve(url).func.__name__,
                          GetBookings.as_view().__name__)

    def test_single_booking_url_resolves(self):
        url = reverse('booking', args=['pk'])
        self.assertEquals(resolve(url).func.__name__,
                          GetBooking.as_view().__name__)

    def test_barber_booking_url_resolves(self):
        url = reverse('barber-booking', args=['pk'])
        self.assertEquals(resolve(url).func.__name__,
                          GetBarberBooking.as_view().__name__)

    def test_user_booking_url_resolves(self):
        url = reverse('user-booking', args=['pk'])
        self.assertEquals(resolve(url).func.__name__,
                          GetUserBooking.as_view().__name__)

    def test_create_booking_url_resolves(self):
        url = reverse('create-booking')
        self.assertEquals(resolve(url).func.__name__,
                          CreateBooking.as_view().__name__)

    def test_update_booking_url_resolves(self):
        url = reverse('update-booking', args=['pk'])
        self.assertEquals(resolve(url).func.__name__,
                          UpdateBooking.as_view().__name__)
