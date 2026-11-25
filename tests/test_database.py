from app.utils.database import (
    create_table,
    clear_students,
    add_student,
    get_students,
    update_student,
    delete_student,
    search_student,
    count_students,
    get_students_by_course,
    safe_add_student,
    transfer_student_course,
    backup_database
)

print("\n--- DATABASE TEST ---")

create_table()
clear_students()

add_student(101, "Ananya", "Computer Science", "ananya@gmail.com")
add_student(102, "Rahul", "Information Technology", "rahul@gmail.com")

print("\nAll Students:")
print(get_students())

print("\nSearch Student:")
print(search_student(101))

print("\nUpdate Student:")
update_student(101, "Ananya", "Computer Science", "ananya123@gmail.com")
print(search_student(101))

print("\nDelete Student:")
delete_student(102)

print("\nFinal Student List:")
print(get_students())

print("\n--- DATABASE COUNT TEST ---")
print("Total students:", count_students())

print("\n--- COURSE SEARCH TEST ---")
print(get_students_by_course("Computer Science"))

print("\n--- DUPLICATE STUDENT TEST ---")
safe_add_student(101, "Duplicate", "Computer Science", "duplicate@gmail.com")

print("\n--- TRANSACTION TEST ---")
transfer_student_course(101, "Data Science")
print(search_student(101))

print("\n--- DATABASE BACKUP TEST ---")
backup_database()
