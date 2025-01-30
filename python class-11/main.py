class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

class Dog(Animal):
    def __init__(self,name, breed):
        super().__init__(name)
        self.breed = breed

    def bark(self):
        print(f"{self.name} is barking.")

dog1 = Dog("buddy", "Golden Retriever")
dog1.eat()
dog1.bark()

from abc import ABC, abstractmethod

class vehicle(ABC):
    @abstractmethod
    
    def start_engine(self):
        pass

class Car(vehicle):
    def start_engine(self):
        print("Car engine started")

class Motorcycle(vehicle):
    def start_engine(self):
        print("Motorcycle engine started")

carObj = Car()
carObj.start_engine()
motorcycleObj = Motorcycle()
motorcycleObj.start_engine()

from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Woof!"

    def walk(self):
        print("Walking...")  

class Cat(Animal):
    def __init__(self, name):
        self.name = name

    def sound(self):
        return f"{self.name}Meow!"
    
    def walk(self):
        print(f"{self.name} is walking...")

dog = Dog()
cat = Cat("Fluffy")

print(dog.sound())
print(cat.sound())
dog.walk()
cat.walk()
