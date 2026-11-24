
from app.core.descriptors import (
    NameDescriptor,
    EmailDescriptor,
    AgeDescriptor
)


class Student:
    name = NameDescriptor()
    email = EmailDescriptor()
    age = AgeDescriptor()


# Creating a student object
student = Student()

# Assigning valid values
student.name = "Theertha"
student.email = "theertha@gmail.com"
student.age = 21

# Displaying student details
print("Name:", student.name)
print("Email:", student.email)
print("Age:", student.age)


print("\n--- Testing Invalid Values ---")

# Test 1: Empty name
try:
    student.name = ""
except ValueError as e:
    print("Name Error:", e)


# Test 2: Invalid email
try:
    student.email = "theertha123"
except ValueError as e:
    print("Email Error:", e)


# Test 3: Age below 16
try:
    student.age = 12
except ValueError as e:
    print("Age Error:", e)


# Test 4: Age above 80
try:
    student.age = 90
except ValueError as e:
    print("Age Error:", e)
