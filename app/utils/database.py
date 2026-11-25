import sqlite3


def create_connection():
    return sqlite3.connect("campushub.db")


def create_table():
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            student_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            course TEXT NOT NULL,
            email TEXT
        )
    """)

    connection.commit()
    connection.close()
    print("Student table created successfully")


def add_student(student_id, name, course, email):
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO students (student_id, name, course, email)
        VALUES (?, ?, ?, ?)
    """, (student_id, name, course, email))

    connection.commit()
    connection.close()
    print("Student added successfully")


def get_students():
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    connection.close()
    return students


def update_student(student_id, name, course, email):
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE students
        SET name = ?, course = ?, email = ?
        WHERE student_id = ?
    """, (name, course, email, student_id))

    connection.commit()
    connection.close()
    print("Student updated successfully")


def delete_student(student_id):
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM students WHERE student_id = ?",
        (student_id,)
    )

    connection.commit()
    connection.close()
    print("Student deleted successfully")


def search_student(student_id):
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM students WHERE student_id = ?",
        (student_id,)
    )

    student = cursor.fetchone()
    connection.close()
    return student
def count_students():
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT COUNT(*) FROM students")
    count = cursor.fetchone()[0]

    connection.close()
    return count


def get_students_by_course(course):
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM students WHERE course = ?",
        (course,)
    )

    students = cursor.fetchall()
    connection.close()
    return students


def safe_add_student(student_id, name, course, email):
    connection = create_connection()

    try:
        cursor = connection.cursor()

        cursor.execute("""
            INSERT INTO students (student_id, name, course, email)
            VALUES (?, ?, ?, ?)
        """, (student_id, name, course, email))

        connection.commit()
        print("Student added successfully")

    except sqlite3.IntegrityError as error:
        print("Database error:", error)

    finally:
        connection.close()

def clear_students():
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute("DELETE FROM students")

    connection.commit()
    connection.close()

    print("Old test records cleared")    

def transfer_student_course(student_id, new_course):
    connection = create_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            "UPDATE students SET course = ? WHERE student_id = ?",
            (new_course, student_id)
        )

        connection.commit()
        print("Course updated successfully")

    except sqlite3.Error as error:
        connection.rollback()
        print("Transaction failed:", error)

    finally:
        connection.close()


def backup_database(backup_file="campushub_backup.db"):
    connection = create_connection()

    with sqlite3.connect(backup_file) as backup:
        connection.backup(backup)

    connection.close()
    print("Database backup created successfully")    