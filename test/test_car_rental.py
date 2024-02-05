import unittest

from src.car_rental import CarRental


class TestCarRental(unittest.TestCase):
    def setUp(self):
        self.car_rental = CarRental(10)

    def test_initial_stock(self):
        self.assertEqual(self.car_rental.display_available_cars(), 10)

    def test_rent_hourly_valid(self):
        time = self.car_rental.rent_on_basis(2, "hourly")
        self.assertIsNotNone(time)
        self.assertEqual(self.car_rental.stock, 8)

    def test_rent_hourly_invalid(self):
        self.assertIsNone(self.car_rental.rent_on_basis(-1, "hourly"))
