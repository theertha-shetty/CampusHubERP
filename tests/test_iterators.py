from app.utils.iterators import (
    NumberIterator,
    number_generator,
    student_id_generator,
    even_number_generator
)

print("\n--- ITERATOR TEST ---")

numbers = NumberIterator([10, 20, 30, 40, 50])

for number in numbers:
    print(number)


print("\n--- GENERATOR TEST ---")

for number in number_generator([10, 20, 30, 40, 50]):
    print(number)


print("\n--- GENERATOR EXPRESSION TEST ---")

squares = (number ** 2 for number in range(1, 6))

for square in squares:
    print(square)


print("\n--- STUDENT ID GENERATOR TEST ---")

for student_id in student_id_generator(101, 5):
    print(student_id)


print("\n--- EVEN NUMBER GENERATOR TEST ---")

for number in even_number_generator(20):
    print(number)