class Customer:
    def __init__(self):
        self.rental_time = None
        self.rental_basis = None
        self.number_of_cars = 0

    def request_car(self):
        cars = int(input("How many cars would you like to rent? "))
        return cars

    def return_car(self):
        if self.rental_time and self.rental_basis and self.number_of_cars:
            return self.rental_time, self.rental_basis, self.number_of_cars
        else:
            return 0, None, 0
