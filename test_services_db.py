from app.database.services import (
    StudentServiceDB,
    FacultyServiceDB,
    CourseServiceDB,
    EnrollmentServiceDB
)

services = [
    StudentServiceDB(),
    FacultyServiceDB(),
    CourseServiceDB(),
    EnrollmentServiceDB()
]

names = ["Students", "Faculty", "Courses", "Enrollments"]

for name, service in zip(names, services):
    try:
        records = service.get_all()
        print(f"{name}: {len(records)} records found")
    finally:
        service.close()