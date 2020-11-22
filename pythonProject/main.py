
class Car:
    wheels = -1
    colour = "blah"

    def my_info(self):
        print(self.wheels)
        print(self.colour)

car1 = Car()
car1.wheels = 4
car1.colour = "blue"

car1.my_info()

car2 = Car()
car2.wheels = 5
car2.colour = "red"

car2.my_info()
