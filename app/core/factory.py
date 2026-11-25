from app.models.student import Student
from app.models.faculty import Faculty
from app.models.course import Course


class EntityFactory:

    @staticmethod
    def create_entity(entity_type, **kwargs):

        if entity_type.lower() == "student":
            return Student(**kwargs)

        elif entity_type.lower() == "faculty":
            return Faculty(**kwargs)

        elif entity_type.lower() == "course":
            return Course(**kwargs)

        else:
            raise ValueError("Invalid entity type")
        