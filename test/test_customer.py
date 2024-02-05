import unittest
from datetime import datetime
from src.customers import Customer


class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer()

    def test_request_car(self):
        self.customer.number_of_cars = 3
        # Input 3
        self.assertEqual(self.customer.request_car(), 3)

    def test_return_car(self):
        self.customer.rental_time = datetime.now()
        self.customer.rental_basis = "weekly"
        self.customer.number_of_cars = 2
        returned = self.customer.return_car()
        self.assertEqual(returned, (self.customer.rental_time, "weekly", 2))
