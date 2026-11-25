import sqlite3

connection = sqlite3.connect("campushub.db")
cursor = connection.cursor()

for table in ["students", "faculty", "courses", "enrollments"]:
    print(f"\n--- {table.upper()} ---")
    cursor.execute(f"SELECT * FROM {table}")

    for row in cursor.fetchall():
        print(row)

connection.close()