# oop_04_polymorphism.py
# Demonstrates: Polymorphism via method overriding, duck typing

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")


class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks.")


class Cat(Animal):
    def speak(self):
        print(f"{self.name} meows.")


class Bird(Animal):
    def speak(self):
        print(f"{self.name} chirps.")


# Polymorphism: the same interface (speak) works for all types
animals = [
    Dog("Rex"),
    Cat("Whiskers"),
    Bird("Tweety"),
    Animal("Unknown"),
]

print("--- All animals speak ---")
for animal in animals:
    animal.speak()      # correct method called automatically based on type

# -------------------------------------------------------------------
# Duck typing: Python does not require a common base class.
# Any object with a speak() method works here.
# -------------------------------------------------------------------

class Robot:
    def __init__(self, model):
        self.model = model

    def speak(self):
        print(f"{self.model} says: Beep boop.")


print("\n--- Duck typing example ---")
speakers = [Dog("Rex"), Cat("Whiskers"), Robot("R2D2")]

for speaker in speakers:
    speaker.speak()     # Robot is not an Animal, but it has speak() -- it works
