from restaurant import Restaurant, User
from car import ElectricCar

my_rest = Restaurant("Vasilek1", 'Rus1')
my_rest.describe_restaurant()

jake = User("Jake", "Narrow", 34)
jake.describe_user()

my_tesla1 = ElectricCar('tesla', 'model s', 2016, 80)
print(my_tesla1.get_descriptive_name())
