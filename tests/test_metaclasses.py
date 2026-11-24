
from app.core.metaclasses import ModelMeta


class Student(metaclass=ModelMeta):
    pass


class Faculty(metaclass=ModelMeta):
    pass


print("Student Created At:", Student.created_at)
print("Student Updated At:", Student.updated_at)

print("Faculty Created At:", Faculty.created_at)
print("Faculty Updated At:", Faculty.updated_at)
