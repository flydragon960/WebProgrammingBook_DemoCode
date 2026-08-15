# ch08_05_functions_closures.py
# Section: Functions and Closures
# Topics: def, return, default parameters, closures, lexical scoping

# ------------------------------------------------------------------
# Basic function
# ------------------------------------------------------------------
def greet(name):
    print(f"Hello, {name}")

greet("Alice")   # Output: Hello, Alice

# ------------------------------------------------------------------
# Function with return value
# ------------------------------------------------------------------
def add(a, b):
    return a + b

result = add(5, 3)
print(result)    # Output: 8

# ------------------------------------------------------------------
# Default parameter values
# ------------------------------------------------------------------
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Alice")             # Hello, Alice!
greet("Bob", "Welcome")    # Welcome, Bob!

# ------------------------------------------------------------------
# Closure: inner function captures variable from enclosing scope
# ------------------------------------------------------------------
def outer_function(msg):
    def inner_function():
        print("Message:", msg)    # 'msg' is captured from outer scope
    return inner_function         # return the function, not its result

say_hello = outer_function("Hello from closure!")
say_hello()    # Output: Message: Hello from closure!
