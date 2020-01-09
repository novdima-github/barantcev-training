class Restaurant():
    def __init__(self, rest_name, rest_cuisine):
        self.rest_name = rest_name
        self.rest_cuisine = rest_cuisine
        self.number_served = 0

    def describe_restaurant(self):
        print(f"The restaurant name is {self.rest_name} and cuisine is {self.rest_cuisine}")

    def open_restaurant(self):
        print("The restaurant is opened")

    def set_number_served(self, number_served):
        self.number_served = number_served
        print(f"number of served visitors equal {number_served}")

    def increment_number_served(self, number_served):
        self.number_served += number_served
        print(f"number of served visitors incremented on {number_served}")

class IceCreamStand(Restaurant):
    def __init__(self, rest_name, rest_cuisine):
        super().__init__(rest_name, rest_cuisine)
        self.flavors = ['icecream1', 'icecream2', 'icecrea3']

    def show_icecreams(self):
        print('Stand icecreams: ' + str(self.flavors))


restaurant = Restaurant("Vasilek", 'Rus')
restaurant.describe_restaurant()
print(restaurant.number_served)
restaurant.number_served = 3
print(restaurant.number_served)
restaurant.set_number_served(5)
print(restaurant.number_served)
restaurant.increment_number_served(10)
print(restaurant.number_served)


class User():
    def __init__(self, fn, ln, age):
        self.fn = fn
        self.ln = ln
        self.age =age
        self.login_attempt = 0

    def increment_login_attempts(self, attempts):
        self.login_attempt += attempts
        print(f'Login attempts incremented {attempts}')

    def reset_login_attempts(self):
        self.login_attempt = 0
        print(f'Login attempts reset')

    def show_login_attempts(self):
        print(f'Number of login attempts {self.login_attempt}')

    def describe_user(self):
        print(f'User info: name: {self.fn}, last name: {self.ln}, age: {self.age}')

    def greet_user(self):
        print(f'Hello {self.fn} {self.ln}')

class Admin(User):
    def __init__(self, fn, ln, age):
        super().__init__(fn, ln, age)
        self.priviliges = AdminPriviliges()

    def show_priviliges(self):
        print(self.fn + ' ' + self.ln + " has the next priviliges: " + str(self.priviliges.admin_priviliges))


class Client(User):
    def __init__(self, fn, ln, age):
        super().__init__(fn, ln, age)
        self.priviliges = ClientPriviliges()

    def show_priviliges(self):
        print(self.fn + ' ' + self.ln + " has the next priviliges: " + str(self.priviliges.client_priviliges))


class AdminPriviliges():
    def __init__(self):
        self.admin_priviliges = ["разрешено добавлять сообщения", "«разрешено удалять пользователей»",
                           "«разрешено банить пользователей»"]


class ClientPriviliges():
    def __init__(self):
        self.client_priviliges = ["Client prvilige 1", "Client prvilige 3",
                           "Client prvilige 2"]

    def show_priviliges(self):
        print("This user has the next priviliges: " + str(self.client_priviliges))





me = User('dima', 'nov', 35)
me.describe_user()
me.greet_user()

jake = User("Jake", "Narrow", 34)
jake.describe_user()
print(jake.login_attempt)
jake.show_login_attempts()
jake.increment_login_attempts(3)
print(jake.login_attempt)
jake.show_login_attempts()
jake.reset_login_attempts()
print(jake.login_attempt)
jake.show_login_attempts()

my_stand = IceCreamStand('Stand_1', 'Minsk')
print(my_stand.flavors)
my_stand.show_icecreams()
admin = Admin('Igor', 'Ivanov', 23)
admin.show_priviliges()

client = Client('Bob', 'Marley', 38)
client.show_priviliges()
client.priviliges.show_priviliges()
