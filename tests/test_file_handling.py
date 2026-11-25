from app.utils.file_handling import (
    save_students,
    load_students,
    add_student,
    display_students,
    save_students_csv,
    load_students_csv,
    serialize_students,
    deserialize_students,
    validate_email,
    validate_phone,
    validate_student,
    safe_load_students,
    search_student
)

print("\n--- FILE HANDLING TEST ---")

students = []

students = add_student(
    students, 101, "Ananya", "Computer Science"
)

students = add_student(
    students, 102, "Rahul", "Information Technology"
)

students = add_student(
    students, 103, "Priya", "Computer Science"
)

print("\n--- DISPLAY STUDENTS ---")
display_students(students)

print("\n--- SAVE STUDENTS ---")
save_students(students)

print("\n--- LOAD STUDENTS ---")
loaded_students = load_students()

display_students(loaded_students)

print("\n--- VERIFY STUDENT COUNT ---")
print("Total students:", len(loaded_students))


print("\n--- CSV TEST ---")
save_students_csv(students)
csv_students = load_students_csv()
print(csv_students)

print("\n--- PICKLE TEST ---")
serialize_students(students)
pickle_students = deserialize_students()
display_students(pickle_students)

print("\n--- REGEX TEST ---")
print("Valid email:", validate_email("student@gmail.com"))
print("Invalid email:", validate_email("student@gmail"))
print("Valid phone:", validate_phone("9876543210"))
print("Invalid phone:", validate_phone("12345"))

print("\n--- STUDENT VALIDATION TEST ---")
print("Valid student:", validate_student(students[0]))
print("Invalid student:", validate_student({"student_id": 104}))

print("\n--- SAFE FILE LOADING TEST ---")
print(safe_load_students())

print("\n--- SEARCH STUDENT TEST ---")
print(search_student(students, 102))
print(search_student(students, 999))