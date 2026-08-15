# ch08_07_exception_handling.py
# Section: Exception Handling
# Topics: try/except/else/finally, multiple exceptions, raise

# ------------------------------------------------------------------
# Basic try / except / else / finally
# ------------------------------------------------------------------
try:
    x = int(input("Enter a number: "))
    result = 10 / x
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Invalid input -- please enter a number.")
else:
    print("Result:", result)      # runs only if no exception occurred
finally:
    print("Execution complete.")  # always runs, exception or not

# ------------------------------------------------------------------
# Raising custom exceptions to enforce business rules
# ------------------------------------------------------------------
def set_age(age):
    if age < 0 or age > 150:
        raise ValueError(f"Invalid age: {age}")
    return age

try:
    set_age(-5)
except ValueError as e:
    print(e)    # Invalid age: -5
