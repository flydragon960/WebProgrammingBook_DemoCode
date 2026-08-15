# ch08_03_data_types.py
# Section: Python Data Types
# Topics: variable declaration, type(), dynamic typing, type hints, input conversion

# ------------------------------------------------------------------
# Variable declaration and assignment
# ------------------------------------------------------------------
x = 10            # int
name = "Alice"    # str
pi = 3.14         # float
is_active = True  # bool

# Confirm types at runtime
print(type(x))          # <class 'int'>
print(type(name))       # <class 'str'>
print(type(is_active))  # <class 'bool'>

# ------------------------------------------------------------------
# Dynamic typing: same variable, different types
# ------------------------------------------------------------------
x = 10
print(type(x))  # <class 'int'>

x = "Now I'm a string!"
print(type(x))  # <class 'str'>

# ------------------------------------------------------------------
# Type hints (Python 3.5+): annotate without enforcing
# ------------------------------------------------------------------
def add(a: int, b: int) -> int:
    return a + b

print(add(3, 4))   # 7

# ------------------------------------------------------------------
# Input conversion: input() always returns str
# ------------------------------------------------------------------
age = int(input("Enter your age: "))
print(f"Next year you will be {age + 1}.")
