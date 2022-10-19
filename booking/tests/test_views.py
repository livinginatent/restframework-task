from django.test import TestCase, Client
from django.urls import reverse
from booking.models import Booking
from user.models import User
from barber.models import Barber


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.bookings_url = reverse('bookings')
        self.single_booking_url = reverse('booking', args=['1'])
        self.create_booking_url = reverse('create-booking')
        self.update_booking_url = reverse('update-booking', args=['1'])
        self.user_booking_url = reverse('user-booking', args=['1'])
        self.barber_booking_url = reverse('barber-booking', args=['1'])
        self.user1 = User.objects.create(
            first_name='test',
            last_name='test1',
            email='2@2.com',
            mobile='444'
        )
        self.barber1 = Barber.objects.create(
            name='test',
            address='london',
            phone='444'
        )
        self.booking1 = Booking.objects.create(
            customer=self.user1,
            barber=self.barber1,
            timeslot='2022-12-12'
        )

    def test_all_bookings_view(self):
        response = self.client.get(self.bookings_url)
        self.assertEquals(response.status_code, 200)

    def test_single_booking_view(self):

        response = self.client.get(self.single_booking_url)
        self.assertEquals(response.status_code, 200)

    def test_create_booking_view(self):
        client = Client()
        response = client.get(self.create_booking_url)
        self.assertEquals(response.status_code, 200)

    def test_update_booking_view(self):
        client = Client()
        response = client.put(self.update_booking_url)
        self.assertEquals(response.status_code, 200)

    def test_user_booking_view(self):
        client = Client()
        response = client.get(self.user_booking_url)
        self.assertEquals(response.status_code, 200)

    def test_barber_booking_view(self):
        client = Client()
        response = client.get(self.barber_booking_url)
        self.assertEquals(response.status_code, 200)
