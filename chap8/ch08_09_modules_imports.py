# ch08_09_modules_imports.py
# Section: Modules and Imports
# Topics: import, from...import, alias, __name__ == "__main__"

# ------------------------------------------------------------------
# Importing the entire module
# ------------------------------------------------------------------
import math
print(math.sqrt(25))     # 5.0
print(math.floor(3.7))   # 3

# ------------------------------------------------------------------
# Importing specific names from a module
# ------------------------------------------------------------------
from math import pi, sin
print(pi)                # 3.141592653589793
print(sin(pi / 2))       # 1.0

# ------------------------------------------------------------------
# Module alias to reduce typing
# ------------------------------------------------------------------
import datetime as dt
now = dt.datetime.now()
print(now)    # e.g., 2025-09-01 14:23:05.123456

# ------------------------------------------------------------------
# __name__ guard: run code only when executed directly, not imported
# ------------------------------------------------------------------
def main():
    print("Running as a script.")

if __name__ == "__main__":
    main()    # Only executes when this file is run directly
