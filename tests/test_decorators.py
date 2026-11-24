
from app.utils.decorators import log_operation


@log_operation
def add_student(name):
    print("Adding student:", name)
    return "Student added successfully"


result = add_student("Theertha")

print(result)

