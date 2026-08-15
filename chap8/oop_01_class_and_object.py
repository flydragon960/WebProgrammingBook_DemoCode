# oop_01_class_and_object.py
# Demonstrates: Class definition, __init__ constructor, instance attributes, methods

class Dog:
    def __init__(self, name, breed):
        self.name = name      # instance attribute
        self.breed = breed    # instance attribute

    def bark(self):
        print(f"{self.name} says: Woof!")

    def describe(self):
        print(f"{self.name} is a {self.breed}.")


# Create objects (instances) from the class
dog1 = Dog("Rex", "Labrador")
dog2 = Dog("Bella", "Poodle")

dog1.bark()       # Rex says: Woof!
dog2.bark()       # Bella says: Woof!
dog1.describe()   # Rex is a Labrador.
dog2.describe()   # Bella is a Poodle.

# Each object has its own independent data
print(dog1.name)  # Rex
print(dog2.name)  # Bella
