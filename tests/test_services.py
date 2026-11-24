
from app.services.student_service import StudentService
from app.services.faculty_service import FacultyService
from app.services.course_service import CourseService
from app.services.enrollment_service import EnrollmentService


# Create service objects
student_service = StudentService()
faculty_service = FacultyService()
course_service = CourseService()
enrollment_service = EnrollmentService()


# Add Student
student_service.add_student(
    "ST101", "Theertha", 21,
    "theertha@gmail.com", "Computer Science"
)

# Add Faculty
faculty_service.add_faculty(
    "FC101", "Rahul", 35,
    "rahul@gmail.com", "Computer Science"
)


print("\n--- COMPUTER SCIENCE FACULTY ---")

cs_faculty = faculty_service.get_faculty_by_department(
    "Computer Science"
)

for faculty in cs_faculty:
    faculty.display_details()


# Add Course
course_service.add_course(
    "CS101", "Python Programming", 4
)


# Enroll Student
enrollment_service.enroll_student("ST101", "CS101")


print("\n--- ALL STUDENTS ---")
for student in student_service.get_all_students():
    student.display_details()

print("\n--- ALL FACULTY ---")
for faculty in faculty_service.get_all_faculty():
    faculty.display_details()

print("\n--- ALL COURSES ---")
for course in course_service.get_all_courses():
    course.display_details()

print("\n--- ALL ENROLLMENTS ---")
for enrollment in enrollment_service.get_all_enrollments():
    enrollment.display_details()


print("\n--- COURSES WITH 4 CREDITS ---")

four_credit_courses = course_service.get_courses_by_credits(4)

for course in four_credit_courses:
    course.display_details()


print("\n--- ALL COURSE NAMES ---")

print(course_service.list_course_names())


print("\n--- ENROLLMENTS FOR ST101 ---")

student_enrollments = enrollment_service.get_enrollments_by_student(
    "ST101"
)

for enrollment in student_enrollments:
    enrollment.display_details()

