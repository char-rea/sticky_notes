# SQLite code for creating a table, inserting records, 
# and performing various operations

import sqlite3

# Creates or opens a file called student_db with an SQLite3 DB
db = sqlite3.connect("student_db.db")

cursor = db.cursor() # Get a cursor object to execute SQL commands

# Create table called python_programming with columns id, name, and grade
cursor.execute('''
    CREATE TABLE IF NOT EXISTS python_programming (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        grade TEXT NOT NULL
    )
''')

# Insert multiple records into the python_programming table
students = [
    (55, 'Carl David', '61'),
    (66, 'Dennis Fredrickson', '88'),
    (77, 'Jane Richards', '78'),
    (12, 'Peyton Sawyer', '45'),
    (2, 'Lucas Brooke', '99')
]

cursor.executemany('''
    INSERT OR REPLACE INTO python_programming (id, name, grade) VALUES (?, ?, ?)
''', students)

# Select all records from the python_programming table
cursor.execute('SELECT * FROM python_programming')
records = cursor.fetchall()
for record in records:
    if 60 <= int(record[2]) <= 80:
        print(record)

# Update the grade for a specific student
cursor.execute('''
    UPDATE python_programming
    SET grade = '65'
    WHERE name = 'Carl David'
''')
print("Updated grade for Carl David.")

# Delete a specific student record from the python_programming table
cursor.execute('''
    DELETE FROM python_programming WHERE name = 'Dennis Fredrickson'
''')
print ("Deleted record for Dennis Fredrickson.")

# Update the grade for all students with an ID greater than 55
cursor.execute('''
    UPDATE python_programming
    SET grade = '80'
    WHERE id > 55
''')
print ("Updated grades for students with ID greater than 55.")

# Commit the changes to the database to ensure they are saved
db.commit()

# Close the database connection when done
db.close()
