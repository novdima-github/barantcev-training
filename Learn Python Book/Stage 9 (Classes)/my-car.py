from car_classes import Car, ElectricCar

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
my_tesla.battery.show_battery_charge()
my_tesla.battery.update_battery()
my_tesla.battery.show_battery_charge()
