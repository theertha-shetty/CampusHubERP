
from app.models.course import Course
from app.utils.decorators import log_operation


class CourseService:

    def __init__(self):
        self.courses = []

    @log_operation
    def add_course(self, course_code, course_name, credits):

        course = Course(
            course_code,
            course_name,
            credits
        )

        self.courses.append(course)

        return course

    def get_all_courses(self):
        return self.courses


    def get_courses_by_credits(self, credits):

        return list(
            filter(
                lambda course: course.credits == credits,
                self.courses
            )
        )


    def list_course_names(self):

        course_names = list(
            map(
                lambda course: course.course_name.upper(),
                self.courses
            )
        )

        return course_names
