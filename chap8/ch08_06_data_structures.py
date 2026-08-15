# ch08_06_data_structures.py
# Section: Data Structures
# Topics: list, tuple, dictionary, set

# ------------------------------------------------------------------
# LIST (Ordered and Mutable)
# ------------------------------------------------------------------
fruits = ["apple", "banana", "cherry"]
print(fruits[0])           # Access by index -> apple
print(fruits[-1])          # Negative index from end -> cherry
fruits.append("orange")    # Add to end
fruits.insert(1, "mango")  # Insert at position 1
print(fruits)              # ['apple', 'mango', 'banana', 'cherry', 'orange']
print(len(fruits))         # Number of items -> 5

# ------------------------------------------------------------------
# TUPLE (Ordered and Immutable)
# ------------------------------------------------------------------
coordinates = (10, 20)
print(coordinates[1])      # Access by index -> 20
# coordinates[0] = 5       # TypeError: tuples are immutable

# ------------------------------------------------------------------
# DICTIONARY (Key-Value Pair Mapping)
# ------------------------------------------------------------------
person = {"name": "Alice", "age": 25}
print(person["name"])        # Access by key -> Alice
person["age"] = 26           # Update existing key
person["email"] = "a@b.com"  # Add new key
print(person)                # {'name': 'Alice', 'age': 26, 'email': 'a@b.com'}

# Safe access with .get() -- returns None instead of raising KeyError
print(person.get("phone"))   # None

# ------------------------------------------------------------------
# SET (Unordered Collection of Unique Items)
# ------------------------------------------------------------------
colors = {"red", "green", "blue"}
colors.add("yellow")
colors.add("red")            # Duplicate ignored
print(colors)                # {'red', 'green', 'blue', 'yellow'} (order may vary)

# Membership test (very fast compared to lists)
print("green" in colors)     # True

# Set operations
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a & b)   # Intersection -> {3, 4}
print(a | b)   # Union        -> {1, 2, 3, 4, 5, 6}
print(a - b)   # Difference   -> {1, 2}
