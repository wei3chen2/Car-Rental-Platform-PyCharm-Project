from datetime import datetime


class CarRental:
    hourly_price = 10
    daily_price = 40
    weekly_price = 160

    def __init__(self, stock: int = 0):
        self.stock = stock

    def display_available_cars(self) -> int:
        print(f"Total available cars: {self.stock}")
        return self.stock

    def rent_on_basis(self, num_cars_to_rent: int, rental_basis: str) -> datetime:
        # Make sure there are cars to rent
        if num_cars_to_rent <= 0:
            print("Number of cars should be positive!")
        elif num_cars_to_rent > self.stock:
            print(f"Sorry, we currently only have {self.stock} cars available to rent")
        else:
            rental_time = datetime.now()
            print(
                f"You have successfully checked out {num_cars_to_rent} cars on a {rental_basis} today at {rental_time}"
            )
            # self.stock = self.stock - number_of_cars
            self.stock -= num_cars_to_rent
            return rental_time

    def return_car(self, rental_time: datetime, rental_basis: str, number_of_cars: int):
        if rental_time and rental_basis and number_of_cars:
            self.stock += number_of_cars
            return_time = datetime.now()
            rental_period = return_time - rental_time

            # Calculate the bill
            bill = self.__calculate_bill(rental_basis, rental_period, number_of_cars)

            print(f"Thanks for returning your car. Your total bill is ${bill}")
        else:
            print("Invalid return.")

    def __calculate_bill(self, rental_basis, rental_period, number_of_cars):
        bill = 0
        if rental_basis == "hourly":
            bill += rental_period.seconds / 3600 * self.hourly_price * number_of_cars
        elif rental_basis == "daily":
            bill += rental_period.days * self.daily_price * number_of_cars
        elif rental_basis == "weekly":
            bill += rental_period.days / 7 * self.weekly_price * number_of_cars
        else:
            raise ValueError("Invalid rental basis")
        return bill
