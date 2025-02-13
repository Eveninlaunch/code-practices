import datetime

class CarRental:  # class to build car rental shop.

    def __init__(self,stock=0):
        self.stock = stock

    def display_stock(self):  # display available cars for rent currnetly.
        print("We currently have {} cars available to rent.".format(self.stock))
        return self.stock

    def rent_car_hourly(self,n):    # rent "n" cars hourly
        if n <= 0:
            print("Sorry, the number of cars should be positive.")
            return None

        elif n > self.stock:
            print("Sorry, we currently have {} cars available to rent.".format(self.stock))
            return None

        else:
            now = datetime.datetime.now()
            print("You have rented a {} car(s) on hourly basis today at {} hours.".format(n,now.hour))
            print("You will be charged $10 for each hour per car.")
            print("We hope that you enjoy our service.")

            self.stock -= n
            return now

    def rent_car_daily(self,n):    # rent "n" cars daily
        if n <= 0:
            print("Sorry, the number of cars should be positive.")
            return None

        elif n > self.stock:
            print("Sorry, we currently have {} cars available to rent.".format(self.stock))
            return None

        else:
            now = datetime.datetime.now()
            print("You have rented a {} car(s) on hourly basis today at {} hours.".format(n, now.hour))
            print("You will be charged $180 for each day per car.")
            print("We hope that you enjoy our service.")

            self.stock -= n
            return now

    def rent_car_weekly(self,n):    # rent "n" cars weekly
        if n <= 0:
            print("Sorry, the number of cars should be positive.")
            return None

        elif n > self.stock:
            print("Sorry, we currently have {} cars available to rent.".format(self.stock))
            return None

        else:
            now = datetime.datetime.now()
            print("You have rented a {} car(s) on hourly basis today at {} hours.".format(n, now.hour))
            print("You will be charged $900 for each week per car.")
            print("We hope that you enjoy our service.")

            self.stock -= n
            return now

    def return_car(self,request):   # return cars from customer, rebalance the stock, make a bill
        rental_time, rental_basis, num_of_cars = request
        bill = 0
        if rental_time and rental_basis and num_of_cars:
            self.stock += num_of_cars
            now = now = datetime.datetime.now()
            rental_period = now - rental_time

            # hourly bill calculation
            if rental_basis == 1:
                bill = round(rental_period.seconds / 3600) * 10 * num_of_cars

            # daily bill calculation
            elif rental_basis == 2:
                bill = round(rental_period.days) * 180 * num_of_cars

            # weekly bill calculation
            elif rental_basis == 3:
                bill = round(rental_period.days / 7) * 900 * num_of_cars

            print("Thanks for returning your car.")
            print("That would be ${}".format(bill))
            print("Hope you enjoy our service.")
            return bill
        else:
            print("Are you sure you rented a car with us?")
            return None


class Customer: # class to build customer object.

    def __init__(self): #
        self.cars = 0
        self.rental_basis = 0
        self.rental_time = 0
        self.bill = 0

    def request_car(self):  # num of cars request
        cars = input("How many cars would you like to rent?")
        try:
            cars = int(cars)
        except ValueError:
            print("Sorry, that's not a positive integer!")
            return -1

        if cars < 1:
            print("Sorry, the number of cars should be positive.")
            return -1
        else:
            self.cars = cars
        return self.cars

    def return_car(self):   # return cars
        if self.rental_basis and self.rental_time and self.cars:
            return self.rental_time, self.rental_basis, self.cars
        else:
            return 0, 0, 0