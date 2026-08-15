# ch08_01_basics.py
# Section: Python Basics
# Topics: Hello World, comments, docstrings, input/output, f-strings

# ------------------------------------------------------------------
# Hello World
# ------------------------------------------------------------------
print("Hello, World!")
print("The answer is", 42)   # multiple values: space-separated

# ------------------------------------------------------------------
# Single-line comments
# ------------------------------------------------------------------
print("Hello, World!")  # Output a greeting message to the console

# ------------------------------------------------------------------
# Docstrings and accessing them at runtime
# ------------------------------------------------------------------
def add(a, b):
    """
    Returns the sum of two numbers.

    Parameters:
        a (int or float): First number
        b (int or float): Second number

    Returns:
        int or float: The sum of a and b
    """
    return a + b

# Access the docstring directly (press q to exit if help() opens a pager)
print(add.__doc__)

# ------------------------------------------------------------------
# Input and Output
# ------------------------------------------------------------------
name = input("Enter your name: ")
print("Hello", name)           # positional: space-separated
print(f"Welcome, {name}!")     # f-string: inline expression

# f-string with format specifier
price = 12.3456
print(f"Formatted price: ${price:.2f}")  # Output: $12.35
