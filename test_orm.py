from app.database.repository import Repository
from app.database.models import CourseDB

repo = Repository()

try:
    course = CourseDB(
        course_code="CS999",
        course_name="ORM Testing",
        credits=3
    )

    repo.add(course)
    print("Course added:", course.course_name)

    courses = repo.get_all(CourseDB)

    print("\nAll courses:")
    for item in courses:
        print(item.course_code, item.course_name)

finally:
    repo.close()