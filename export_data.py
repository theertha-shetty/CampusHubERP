import sqlite3
import json
import os

connection = sqlite3.connect("campushub.db")
cursor = connection.cursor()

os.makedirs("data", exist_ok=True)

tables = ["students", "faculty", "courses", "enrollments"]

for table in tables:
    cursor.execute(f"SELECT * FROM {table}")
    rows = cursor.fetchall()

    columns = [description[0] for description in cursor.description]

    records = [
        dict(zip(columns, row))
        for row in rows
    ]

    with open(f"data/{table}.json", "w") as file:
        json.dump(records, file, indent=4)

    print(f"{table}.json created successfully")

connection.close()