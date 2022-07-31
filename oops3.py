#Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.

class Vehicle :
    def __init__(self,max_speed,mileage):
        self.max_speed = max_speed
        self.mileage = mileage

x = Vehicle(200, 150)

print(x.mileage,x.max_speed)

#Create a Vehicle class without any variables and methods:

print("Speed is : " School_bus.max_speed )

#Create a child class Bus that will inherit all of the variables and methods of the Vehicle class

class Bus(Vehicle) :
    pass

School_bus = Bus(150,300)

print("Speed is : ", School_bus.max_speed )

print("Mileage is : ", School_bus.mileage )










