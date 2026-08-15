# ch08_08_file_handling.py
# Section: File Handling
# Topics: open(), with statement, write, read, encoding

# ------------------------------------------------------------------
# Writing to a file
# "w" mode creates the file or overwrites it if it already exists
# ------------------------------------------------------------------
with open("example.txt", "w", encoding="utf-8") as f:
    f.write("Hello, Python!\n")
    f.write("Second line.\n")

print("File written.")

# ------------------------------------------------------------------
# Reading from a file
# "r" mode is the default; file must already exist
# ------------------------------------------------------------------
with open("example.txt", "r", encoding="utf-8") as f:
    content = f.read()    # read entire file as a single string
    print(content)

# ------------------------------------------------------------------
# Reading line by line (memory-efficient for large files)
# ------------------------------------------------------------------
with open("example.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())   # strip() removes the trailing newline

# ------------------------------------------------------------------
# Appending to a file
# "a" mode adds to the end without overwriting existing content
# ------------------------------------------------------------------
with open("example.txt", "a", encoding="utf-8") as f:
    f.write("Appended line.\n")

print("Line appended.")
