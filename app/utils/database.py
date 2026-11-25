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


def create_all_tables():
    connection = create_connection()
    cursor = connection.cursor()

    # Faculty table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS faculty (
            faculty_id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER,
            email TEXT,
            department TEXT
        )
    """)

    # Courses table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS courses (
            course_code TEXT PRIMARY KEY,
            course_name TEXT NOT NULL,
            credits INTEGER NOT NULL
        )
    """)

    # Enrollments table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS enrollments (
            student_id TEXT NOT NULL,
            course_code TEXT NOT NULL,
            enrollment_date TEXT,
            status TEXT DEFAULT 'Active',
            PRIMARY KEY (student_id, course_code)
        )
    """)

    connection.commit()
    connection.close()

    print("All database tables created successfully")

def add_faculty(faculty_id, name, age, email, department):
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO faculty
        (faculty_id, name, age, email, department)
        VALUES (?, ?, ?, ?, ?)
    """, (faculty_id, name, age, email, department))

    connection.commit()
    connection.close()

    print("Faculty added successfully")

def add_course(course_code, course_name, credits):
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO courses
        (course_code, course_name, credits)
        VALUES (?, ?, ?)
    """, (course_code, course_name, credits))

    connection.commit()
    connection.close()

    print("Course added successfully")


def add_enrollment(student_id, course_code, enrollment_date, status="Active"):
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO enrollments
        (student_id, course_code, enrollment_date, status)
        VALUES (?, ?, ?, ?)
    """, (student_id, course_code, enrollment_date, status))

    connection.commit()
    connection.close()

    print("Enrollment added successfully")