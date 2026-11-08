# ch08_10_ai_judging.py
# Section: Python in the AI Era -- Judging Generated Code
# Topics: mutable default arguments, bare except, failing informatively
# Run: python ch08_10_ai_judging.py

# ------------------------------------------------------------------
# AI's version: one shared list, and a bare except that hides errors
# ------------------------------------------------------------------
def collect_ai(value, bucket=[]):
    try:
        bucket.append(int(value))
    except:
        pass
    return bucket

print(collect_ai("1"))        # [1]
print(collect_ai("2"))        # [1, 2]  <-- the list survived the first call!
print(collect_ai("three"))    # [1, 2]  <-- the error vanished silently

# ------------------------------------------------------------------
# Hardened version
# ------------------------------------------------------------------
def collect(value, bucket=None):
    if bucket is None:              # no shared mutable default
        bucket = []
    try:
        bucket.append(int(value))
    except ValueError:              # catch only what you expect
        raise ValueError(f"Not an integer: {value!r}")   # fail informatively
    return bucket

print(collect("1"))           # [1]
print(collect("2"))           # [2]  a fresh list on every call

try:
    collect("three")
except ValueError as e:
    print(e)                  # Not an integer: 'three'
