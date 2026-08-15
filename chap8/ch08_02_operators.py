# ch08_02_operators.py
# Section: Python Basics - Operators
# Topics: arithmetic, comparison, logical, chained comparisons

# ------------------------------------------------------------------
# Arithmetic operators
# ------------------------------------------------------------------
print(7 / 2)    # 3.5  (true division)
print(7 // 2)   # 3    (floor division)
print(7 % 2)    # 1    (remainder / modulo)
print(2 ** 8)   # 256  (exponentiation)

# ------------------------------------------------------------------
# Comparison and logical operators
# ------------------------------------------------------------------
x = 5
y = 10
print(x < y and y > 5)   # True: both conditions are met
print(x == 5 or y == 5)  # True: first condition is met
print(not x == 5)         # False: x is 5, negated

# ------------------------------------------------------------------
# Chained comparisons
# ------------------------------------------------------------------
age = 20
print(18 < age < 65)   # True: equivalent to age > 18 and age < 65
