from src.car_rental import CarRental
from src.customers import Customer


def main():
    car_rental = CarRental(10)
    customer = Customer()

    while True:
        # COMING FROM FRONTEND
        print(
            """
        ==== Car Rental Shop ====
        1. Display available cars
        2. Request a car on hourly basis: $10/hr
        3. Request a car on daily basis: $40/day
        4. Request a car on weekly basis: $160/week
        5. Return car
        6. Exit
        """
        )
        choice = int(input("Enter choice: "))

        # BACKEND LOGIC
        if choice == 1:
            car_rental.display_available_cars()
        elif choice == 2:
            customer.number_of_cars = customer.request_car()
            customer.rental_basis = "hourly"
            customer.rental_time = car_rental.rent_on_basis(
                customer.number_of_cars, customer.rental_basis
            )
        elif choice == 3:
            customer.number_of_cars = customer.request_car()
            customer.rental_basis = "daily"
            customer.rental_time = car_rental.rent_on_basis(
                customer.number_of_cars, customer.rental_basis
            )
        elif choice == 4:
            customer.number_of_cars = customer.request_car()
            customer.rental_basis = "weekly"
            customer.rental_time = car_rental.rent_on_basis(
                customer.number_of_cars, customer.rental_basis
            )
        elif choice == 5:
            rental_time, rental_basis, number_of_cars = customer.return_car()
            car_rental.return_car(rental_time, rental_basis, number_of_cars)
        elif choice == 6:
            break
        else:
            print("Invalid choice. Please try again.")

    # Some more logic to send confirmation back to front-end.


if __name__ == "__main__":
    main()
