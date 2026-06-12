# import sqlite3
# conn = sqlite3.connect("student.db")

# cursor  = conn.cursor()

# students =[
#     (2,"mohit",21),
#     (3,"yogesh",23),
#     (4,"himanshu",22)
# ]

# cursor.execute(
#     "SELECT * FROM students"
# )

# data = cursor.fetchone()

# for row in data:
#     print(row)

# conn.commit()
# conn.close()

import sqlite3

conn = sqlite3.connect("student.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
)
""")

cursor.execute(
"""
INSERT INTO students(name,age)
VALUES(?,?)
""",
("Mohit",22)
)

conn.commit()

cursor.execute(
"""
SELECT *
FROM students
"""
)

for row in cursor.fetchall():
    print(row)

conn.close()