class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make.title() + ' ' + self.model.title()
        return long_name

    def read_odometer(self):
        print(self.make + " has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
            print(f'Odometer was set on {mileage} miles')
        else:
            print('You cant update odometer with the value less than sat')

    def add_odometer(self, miles):
        self.odometer_reading += miles
        print(f'Odometer was added {miles} miles')

    def class_identification(self):
        print("This object relates to the Car class")


class Battery():
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def get_range(self):
        if self.battery_size ==70:
            range = 250
            message = "This car can go " + str(range) + ' miles on a full charge'
            print(message)
        elif self.battery_size == 80:
            range = 300
            message = "This car can go " + str(range) + ' miles on a full charge'
            print(message)
        else:
            print("Underfined")


class ElectricCar(Car):
    def __init__(self, make, model, year, charge=90):
        super(ElectricCar, self).__init__(make, model, year)
        self.battery = Battery(charge)

    def describe_battery(self):
        print(self.make + ' ' + self.model + ' has ' + str(self.battery.battery_size) + ' -kWh battery')

    def class_identification(self):
        print("This object relates to the ElectricCar class")


my_car = Car('audi', 'a4', 1998)
print(my_car.get_descriptive_name())
my_car.odometer_reading = 13
my_car.read_odometer()
my_car.update_odometer(11)
my_car.read_odometer()
my_car.add_odometer(20)
my_car.read_odometer()

my_tesla = ElectricCar('tesla', 'model s', 2016, 80)
print(my_tesla.get_descriptive_name())

my_tesla.read_odometer()
my_tesla.describe_battery()
my_tesla.class_identification()
my_car.class_identification()
my_tesla.battery.get_range()