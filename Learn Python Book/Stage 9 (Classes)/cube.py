class Die():
    def __init__(self, sides = 6):
        self.sides = sides

    def roll_die(self):
        from random import randint
        x = randint(1, self.sides)
        print(str(x))

my_die = Die(10)
for i in range(10):
    my_die.roll_die()
