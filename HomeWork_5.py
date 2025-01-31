import sqlite3

connect = sqlite3.connect("Students.db")
cursor = connect.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Students(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR (30) NOT NULL,
        age INT DEFAULT NULL,
        grade VARCHAR NOT NULL
    )
""")

# def register():
#     name = input("Введите ФИО: ")
#     age = int(input("Введите возраст: "))
#     grade = input("Введите текущий класс: ")

#     cursor.execute(""" INSERT INTO Students
#                    (name, age, grade)
#                    VALUES (?, ?, ?)""", (name, age, grade))
#     connect.commit()

# def all_students():
#     cursor.execute("SELECT * FROM students WHERE age > 16")
#     students = cursor.fetchone()
#     print(students)

# def name_students(name):
#     cursor.execute("SELECT * FROM Students WHERE name = ?", (name,))
#     student = cursor.fetchall()
#     print(student)

# def update_grade(id):
#     cursor.execute("UPDATE Students SET grade = '11A' WHERE grade = '9A' AND id = ?", (id,))
#     connect.commit()
    
# def delete_student(id):
#     cursor.execute("DELETE FROM Students WHERE id = ?",(id,))
#     connect.commit()
#     print(f"Пользователь {id}-id Был удалён!")

# def backend_student():
#     cursor.execute("SELECT * FROM Students ORDER BY name ASC")
#     student = cursor.fetchall()
#     print(student)

# def count_students():
#     cursor.execute("SELECT COUNT(*) FROM Students")
#     count = cursor.fetchone()[0]
#     print(f"В классе {count} учеников!")

# register()
# all_students()
# name_students('Abdulloh')
# update_grade(3)
# delete_student(1)
# backend_student()
# count_students()
