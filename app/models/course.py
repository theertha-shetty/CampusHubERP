
class Course:

    def __init__(self, course_code, course_name, credits):
        self.course_code = course_code
        self.course_name = course_name
        self.credits = credits

    def display_details(self):
        print("Course Code:", self.course_code)
        print("Course Name:", self.course_name)
        print("Credits:", self.credits)

    def to_dict(self):
        return {
            "course_code": self.course_code,
            "course_name": self.course_name,
            "credits": self.credits
        }

