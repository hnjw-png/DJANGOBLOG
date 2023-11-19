from django.test import TestCase


class TestDjango(TestCase):

    def test_title_is_required(self):
        form = ReservationForm ({'title': ''})
        self.assertFalse(form.is_valid())

