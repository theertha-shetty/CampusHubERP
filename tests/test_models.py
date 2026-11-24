
from app.models.student import Student
from app.models.faculty import Faculty
from app.models.course import Course
from app.models.enrollment import Enrollment


# Create Student
student = Student(
    "ST101",
    "Theertha",
    21,
    "theertha@gmail.com",
    "Computer Science"
)

# Create Faculty
faculty = Faculty(
    "FC101",
    "Rahul",
    35,
    "rahul@gmail.com",
    "Computer Science"
)

# Create Course
course = Course(
    "CS101",
    "Python Programming",
    4
)

# Create Enrollment
enrollment = Enrollment("ST101", "CS101")


print("\n--- STUDENT DETAILS ---")
student.display_details()

print("\n--- FACULTY DETAILS ---")
faculty.display_details()

print("\n--- COURSE DETAILS ---")
course.display_details()

print("\n--- ENROLLMENT DETAILS ---")
enrollment.display_details()


print("\n--- STUDENT DICTIONARY ---")
print(student.to_dict())


print("\n--- TESTING INVALID STUDENT DATA ---")

try:
    invalid_student = Student(
        "ST102",
        "",
        21,
        "invalidemail",
        "Computer Science"
    )
except ValueError as e:
    print("Validation Error:", e)


print("\n--- TESTING INVALID EMAIL ---")

try:
    invalid_student = Student(
        "ST103",
        "Aarav",
        21,
        "invalidemail",
        "Computer Science"
    )
except ValueError as e:
    print("Validation Error:", e)


print("\n--- TESTING INVALID AGE ---")

try:
    invalid_student = Student(
        "ST104",
        "Aarav",
        12,
        "aarav@gmail.com",
        "Computer Science"
    )
except ValueError as e:
    print("Validation Error:", e)

