# oop_03_inheritance.py
# Demonstrates: Single inheritance, super(), method overriding, extending parent behaviour

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print(f"{self.name} makes a sound.")

    def describe(self):
        print(f"{self.name} is {self.age} years old.")


class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)   # call parent constructor
        self.breed = breed            # add child-specific attribute

    def speak(self):                  # override parent method
        print(f"{self.name} barks.")

    def fetch(self):                  # new method specific to Dog
        print(f"{self.name} fetches the ball!")


class Cat(Animal):
    def __init__(self, name, age, indoor):
        super().__init__(name, age)
        self.indoor = indoor

    def speak(self):                  # override parent method
        print(f"{self.name} meows.")

    def describe(self):               # extend parent method
        super().describe()            # call parent version first
        status = "indoor" if self.indoor else "outdoor"
        print(f"{self.name} is an {status} cat.")


# Using the classes
dog = Dog("Rex", 3, "Labrador")
cat = Cat("Whiskers", 5, indoor=True)

dog.speak()       # Rex barks.
dog.describe()    # Rex is 3 years old.  (inherited from Animal)
dog.fetch()       # Rex fetches the ball!

cat.speak()       # Whiskers meows.
cat.describe()    # Whiskers is 5 years old. / Whiskers is an indoor cat.

# Check inheritance
print(isinstance(dog, Dog))     # True
print(isinstance(dog, Animal))  # True -- Dog IS an Animal
print(isinstance(cat, Dog))     # False
