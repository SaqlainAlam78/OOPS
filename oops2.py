#Example 1: Creating a class and object with class and instance attributes

class dog :
    atr1 = "mammal"

    def __init__(self,name) :
        self.name = name

tom = dog("tom")
groot = dog("groot")

print("the name of my dog is {}".format(tom.name))
print("Tom is a {}".format(tom.atr1))


#Example 2: Creating Class and objects with methods

class dog :
    atr1 = "mammal"

    def __init__(self,name) :
        self.name = name

    def speak(self):
        print("My name is {}".format(self.name))

tom = dog("tom")
groot = dog("groot")

tom.speak()
groot.speak()

#Example: Inheritance in Python

class person(object) :
    def __init__(self,name,id_number):
        self.name = name
        self.id_number = id_number

    def display(self):
        print(self.name)
        print(self.id_number)

class employee(person) :

    def __init__(self,name,id_number,salary,age):
        self.salary = salary
        self.age = age

        person.__init__(self,name,id_number)

    def details(self):
        print("My name is {}".format(self.name))
        print("IdNumber: {}".format(self.id_number))
        print("Salary: {}".format(self.salary))

a = employee('Raj','1899','20000','25')

a.display()
a.details()
















