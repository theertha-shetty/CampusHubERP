
# Normal function
def calculate_square(number):
    return number * number


# Lambda function
square = lambda number: number * number


print("Normal Function:", calculate_square(5))
print("Lambda Function:", square(5))


# Using lambda with map()
marks = [70, 80, 90, 60, 85]

updated_marks = list(map(lambda mark: mark + 5, marks))

print("Updated Marks:", updated_marks)


# Using filter()
marks = [35, 80, 45, 90, 25, 70]

passed_marks = list(
    filter(lambda mark: mark >= 50, marks)
)

print("Passed Marks:", passed_marks)


from functools import reduce

marks = [70, 80, 90, 60]

total_marks = reduce(
    lambda total, mark: total + mark,
    marks
)

print("Total Marks:", total_marks)


def student_counter():

    count = 0

    def add_student():
        nonlocal count
        count += 1
        return count

    return add_student


counter = student_counter()

print("Total Students:", counter())
print("Total Students:", counter())
print("Total Students:", counter())


# Using List Comprehension

marks = [70, 80, 90, 60, 85]

passed_marks = [mark for mark in marks if mark >= 50]

print("Passed Marks:", passed_marks)

squared_marks = [mark * mark for mark in marks]

print("Squared Marks:", squared_marks)


from functools import reduce

marks = [70, 80, 90, 60, 85]

total = reduce(
    lambda x, y: x + y,
    marks
)

average = total / len(marks)

print("Total Marks:", total)
print("Average Marks:", average)


print("\n--- ZIP TEST ---")

students = ["Ananya", "Rahul", "Priya"]
departments = ["Computer Science", "Commerce", "Science"]

combined = list(zip(students, departments))

print(combined)

print("\n--- ENUMERATE TEST ---")

students = ["Ananya", "Rahul", "Priya"]

for index, name in enumerate(students):
    print(index, name)

print("\n--- ANY TEST ---")

marks = [35, 45, 67, 80]

print(any(mark >= 50 for mark in marks))    

print("\n--- ALL TEST ---")

marks = [65, 75, 80, 90]

print(all(mark >= 50 for mark in marks))

print("\n--- SORTED TEST ---")

marks = [75, 45, 90, 60, 85]

print("Ascending:", sorted(marks))
print("Descending:", sorted(marks, reverse=True))

print("\n--- REVERSED AND SUM TEST ---")

numbers = [10, 20, 30, 40, 50]

print("Reversed:", list(reversed(numbers)))
print("Total:", sum(numbers))
print("Minimum:", min(numbers))
print("Maximum:", max(numbers))

