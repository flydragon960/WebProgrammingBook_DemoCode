# oop_06_class_vs_instance.py
# Demonstrates: Class attributes, instance attributes,
#               @classmethod, @staticmethod, alternative constructors

class Student:
    school = "McGill University"    # class attribute: shared by all instances
    _count = 0                      # class attribute: track number of students

    def __init__(self, name, grade):
        self.name = name            # instance attribute
        self.grade = grade          # instance attribute
        Student._count += 1         # update class attribute on every new instance

    # ----------------------------------------------------------------
    # Regular instance method: receives the instance (self)
    # ----------------------------------------------------------------
    def report(self):
        status = "Pass" if self.grade >= 50 else "Fail"
        print(f"{self.name} | Grade: {self.grade} | {status} | {Student.school}")

    # ----------------------------------------------------------------
    # Class method: receives the class (cls), not the instance
    # Used here as an alternative constructor
    # ----------------------------------------------------------------
    @classmethod
    def from_string(cls, data_string):
        """Create a Student from a comma-separated string: 'Name,Grade'"""
        name, grade = data_string.split(",")
        return cls(name.strip(), int(grade.strip()))

    @classmethod
    def get_count(cls):
        """Return the total number of Student objects created."""
        return cls._count

    @classmethod
    def get_school(cls):
        return cls.school

    # ----------------------------------------------------------------
    # Static method: no access to class or instance
    # Used for utility functions related to the class
    # ----------------------------------------------------------------
    @staticmethod
    def is_valid_grade(grade):
        """Return True if grade is between 0 and 100."""
        return 0 <= grade <= 100

    @staticmethod
    def letter_grade(grade):
        """Convert a numeric grade to a letter grade."""
        if grade >= 90:
            return "A"
        elif grade >= 80:
            return "B"
        elif grade >= 70:
            return "C"
        elif grade >= 60:
            return "D"
        else:
            return "F"


# --- Using regular constructor ---
s1 = Student("Alice", 88)
s2 = Student("Bob", 45)

# --- Using alternative constructor (class method) ---
s3 = Student.from_string("Charlie, 73")

# --- Instance methods ---
s1.report()     # Alice | Grade: 88 | Pass | McGill University
s2.report()     # Bob   | Grade: 45 | Fail | McGill University
s3.report()     # Charlie | Grade: 73 | Pass | McGill University

print()

# --- Class attributes and methods ---
print(Student.school)           # McGill University
print(Student.get_school())     # McGill University
print(Student.get_count())      # 3  (three students created)

print()

# --- Static methods ---
print(Student.is_valid_grade(85))    # True
print(Student.is_valid_grade(110))   # False
print(Student.letter_grade(88))      # B
print(Student.letter_grade(45))      # F

# Static and class methods are also accessible via an instance
print(s1.letter_grade(s1.grade))     # B
