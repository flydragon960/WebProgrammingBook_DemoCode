# oop_05_abstraction.py
# Demonstrates: Abstract base classes, @abstractmethod, enforced interface

from abc import ABC, abstractmethod


class Shape(ABC):
    """Abstract base class for all shapes. Cannot be instantiated directly."""

    @abstractmethod
    def area(self):
        """Return the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Return the perimeter of the shape."""
        pass

    def describe(self):
        """Concrete method shared by all shapes."""
        print(f"Shape: {self.__class__.__name__}")
        print(f"  Area     : {self.area():.2f}")
        print(f"  Perimeter: {self.perimeter():.2f}")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14159 * self.radius


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a   # three sides
        self.b = b
        self.c = c

    def area(self):
        # Heron's formula
        s = (self.a + self.b + self.c) / 2
        return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5

    def perimeter(self):
        return self.a + self.b + self.c


# Attempting to instantiate the abstract class raises TypeError
try:
    s = Shape()
except TypeError as e:
    print(f"Cannot instantiate Shape: {e}\n")

# All concrete subclasses work through the same interface
shapes = [Circle(5), Rectangle(4, 6), Triangle(3, 4, 5)]

for shape in shapes:
    shape.describe()
    print()
