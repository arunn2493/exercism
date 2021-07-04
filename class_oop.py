# class Dog:
#     '''
#     This is a doc string
#     '''

#     species = "Canis familiaris"

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f"{self.name} is a instance of the class"

#     def description(self):
#         return f"{self.name} is {self.age} years old"

#     def char(self, activity):
#         return f"{self.name} is {self.age} years old and it likes to {activity}"


# a = Dog("a", 1)

# print(Dog.__doc__)
# print(a)
# print(a.description())
# print(a.char("run"))

class Car:

    sound = "Wroom"

    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __str__(self):
        return f"The {self.color} car has {self.mileage} miles."

    def speed(self, speed):
        return f"{self.color} has a speed of {speed}"


class Benz(Car):
    def make(self, make="Mercedes"):
        return f"{self.color} is of make {make}"

    def speed2(self, speed):
        return f"{self.make()} . {super().speed(speed)}"


blue = Benz("blue", 20000)
red = Car("red", 30000)

# print(type(blue))
#  checking if blue is an instance of class CAR
print(isinstance(blue, Car))
# print(isinstance(red, Benz))
# print(blue.sound)
# print(red)
print(blue.make())
print(blue.make("Hyundai"))

print(blue.speed2(25))
