# ch08_04_control_flow.py
# Section: Control Flow Statements
# Topics: if/elif/else, for loop, while loop, break, continue

# ------------------------------------------------------------------
# if / elif / else
# ------------------------------------------------------------------
age = 18
if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teen")
else:
    print("Minor")

# ------------------------------------------------------------------
# for loop with range()
# ------------------------------------------------------------------
# range(5) produces 0, 1, 2, 3, 4
for i in range(5):
    print(i)       # prints 0, 1, 2, 3, 4

# ------------------------------------------------------------------
# while loop
# ------------------------------------------------------------------
count = 0
while count < 5:
    print(count)   # prints 0, 1, 2, 3, 4
    count += 1     # equivalent to count = count + 1

# ------------------------------------------------------------------
# break and continue
# ------------------------------------------------------------------
for i in range(10):
    if i == 3:
        continue   # skip 3
    if i == 7:
        break      # stop at 7
    print(i)       # prints 0, 1, 2, 4, 5, 6
