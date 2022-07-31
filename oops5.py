#Create a Bus child class that inherits from the Vehicle class. The default fare charge of any vehicle is seating capacity * 100. If Vehicle is Bus instance, we need to add an extra 10% on full fare as a maintenance charge. So total fare for bus instance will become the final amount = total fare + 10% of the total fare.

class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    def fare(self):
        amount = super().fare()
        amount += amount * 10 / 100
        return amount
class Car(Vehicle):
    pass

School_bus = Bus("School Volvo", 12, 50)
print("Total Bus fare is:", School_bus.fare())

car = Car("Taxi",12,50)
print("Total Bus fare is:", car.fare())

#Write a program to determine which class a given Bus object belongs to.

class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(Vehicle):
    pass

School_bus = Bus("School Volvo", 12, 50)

print(type(School_bus))


#Determine if School_bus is also an instance of the Vehicle class

class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(Vehicle):
    pass

School_bus = Bus("School Volvo", 12, 50)

# Python's built-in isinstance() function
print(isinstance(School_bus, Vehicle))

#Write a Python class Square, and define two methods that return the square area and perimeter.

class Square :
    def __init__(self,num):
        self.num=num

    def sq_area(self):
        return self.num * self.num
    def perimeter(self):
        return 4 * self.num

a = Square(5)
print(a.sq_area())
print(a.perimeter())

#Write a program that prints the class name using its object.

class Animal():
    pass

lion = Animal()

print("The class name of the object is :",lion.__class__.__name__ )

#Write a Python program that lists out all the default as well as custom properties of the class.

class Animal():
    pass

lion = Animal()

print(dir(Animal))





























