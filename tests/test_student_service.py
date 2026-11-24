
from app.services.student_service import StudentService
from app.models.student import Student

student_service = StudentService()

# Add first student
student_service.add_student(
    "ST101",
    "Theertha",
    21,
    "theertha@gmail.com",
    "Computer Science"
)

# Display all students
print("\n--- ALL STUDENTS ---")

for student in student_service.get_all_students():
    student.display_details()


print("\n--- COMPUTER SCIENCE STUDENTS ---")

cs_students = student_service.get_students_by_department(
    "Computer Science"
)

for student in cs_students:
    student.display_details()


print("\n--- SORTED STUDENT NAMES ---")
print(student_service.list_students())


print("\n--- UPDATING STUDENT ---")

updated = student_service.update_student(
    "ST101",
    "Theertha Shetty",
    21,
    "theertha@gmail.com",
    "Information Technology"
)

print("Student Updated:", updated)


print("\n--- STUDENTS AFTER UPDATE ---")

for student in student_service.get_all_students():
    student.display_details()


print("\n--- REMOVING STUDENT ---")

removed = student_service.remove_student("ST101")

print("Student Removed:", removed)

print("\nRemaining Students:", student_service.get_all_students())


print("\n--- ADMISSION ELIGIBILITY ---")

print(
    "Age 21:",
    StudentService.is_eligible_for_admission(21)
)

print(
    "Age 14:",
    StudentService.is_eligible_for_admission(14)
)

print("\n--- CLASS METHOD ---")

print(StudentService.get_service_name())

print("\n--- STR METHOD TEST ---")

student = StudentService().add_student(
    "ST105", "Ananya", 20,
    "ananya@gmail.com", "Computer Science"
)

print(student)

print("\n--- REPR METHOD TEST ---")

print(repr(student))

print(student)
print(repr(student))

print("\n--- ISINSTANCE TEST ---")

print(isinstance(student, Student))

print("\n--- TYPE TEST ---")

print(type(student))

print("\n--- ISSUBCLASS TEST ---")

print(issubclass(Student, object))

print("\n--- HASATTR TEST ---")

print(hasattr(student, "name"))
print(hasattr(student, "email"))


print("\n--- GETATTR TEST ---")

print(getattr(student, "name"))
print(getattr(student, "email"))


print("\n--- SETATTR TEST ---")

setattr(student, "name", "Ananya Sharma")

print(student.name)


print("\n--- DELATTR TEST ---")

delattr(student, "student_id")
print(hasattr(student, "student_id"))

print("\n--- VARS TEST ---")

print(vars(student))

print("\n--- DIR TEST ---")

print("name" in dir(student))
print("display_details" in dir(student))
print("to_dict" in dir(student))

print("\n--- CALLABLE TEST ---")

print(callable(Student))
print(callable(student))

print("\n--- IS OPERATOR TEST ---")

another_student = student

print(student is another_student)

print("\n--- IS VS EQUALS TEST ---")

another_student = student

print(student == another_student)
print(student is another_student)

print("\n--- ID TEST ---")

print(id(student))
print(id(another_student))

import copy

print("\n--- COPY TEST ---")

copied_student = copy.copy(student)

print(student is copied_student)
print(student.name == copied_student.name)

deep_copied_student = copy.deepcopy(student)

print("\n--- DEEP COPY TEST ---")

print(student is deep_copied_student)
print(student.name == deep_copied_student.name)

print("\n--- SHALLOW VS DEEP COPY ---")

original = [["Python", "Java"], ["HTML", "CSS"]]

shallow = copy.copy(original)
deep = copy.deepcopy(original)

original[0].append("C++")

print("Original:", original)
print("Shallow Copy:", shallow)
print("Deep Copy:", deep)